import factory
from update_view.models import Store
from django.test import TestCase
from django.test.client import Client
from ttools.skyprotests.tests_mixins import ResponseTestsMixin


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store

    slug = "testmarket"
    name = "teststore"
    address = "Тестовая"
    latitude = 777777.39503894
    longitude = 777777.5573879
    email = "test_sky@pro.com"


TEST_URL = "/update_view/1/"


class UpdateViewClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(UpdateViewClassTestCase, cls).setUpClass()
        for _ in range(10):
            StoreFactory.create()

    def setUp(self):
        self.model = Store
        self.student_app = Client()

    def check_field_update_is_correct(self, field, new_value, test_options):
        obj = self.check_status_code_jsonify_and_expected(**test_options).json()
        self.assertTrue(
            obj.get(field) == str(new_value),
            f"Проверьте что при POST-запросе на адрес вида update_view/<id>/ поле {field} обновляется корректно"
        )

    def test_url_works_correct(self):
        self.url = TEST_URL
        test_options = {
            "url": self.url,
            "method": "PATCH",
            "code": [200],
            "student_response": self.student_app.patch(
                self.url,
                data={"name": "new_name"},
                content_type="application/json"
            ),
            "expected": dict,
            "django_mode": True,
        }

        response = self.check_status_code_jsonify_and_expected(**test_options)
        obj = response.json()
        expected_attributes = (field.name for field in self.model._meta.fields)
        self.check_expected_attributes(obj, expected_attributes)

        # проверяем поле name
        self.check_field_update_is_correct("name", "new_name", test_options)

        # проверяем поле email
        field = "email"
        value = "new_email@mail.ru"
        test_options["student_response"] = self.student_app.patch(
                self.url,
                data={field: value},
                content_type="application/json"
            )
        self.check_field_update_is_correct(field, value, test_options)

        # проверяем поле latitude
        field = "latitude"
        value = 555555.39503894
        test_options["student_response"] = self.student_app.patch(
                self.url,
                data={field: value},
                content_type="application/json"
            )
        self.check_field_update_is_correct(field, value, test_options)

        # проверяем поле longitude
        field = "longitude"
        value = 555555.39503894
        test_options["student_response"] = self.student_app.patch(
                self.url,
                data={field: value},
                content_type="application/json"
            )
        self.check_field_update_is_correct(field, value, test_options)

        # проверяем поле slug
        field = "slug"
        value = "new_slug"
        test_options["student_response"] = self.student_app.patch(
                self.url,
                data={field: value},
                content_type="application/json"
            )
        self.check_field_update_is_correct(field, value, test_options)

        # проверяем поле address
        field = "address"
        value = "new_address"
        test_options["student_response"] = self.student_app.patch(
                self.url,
                data={field: value},
                content_type="application/json"
            )
        self.check_field_update_is_correct(field, value, test_options)

        # проверим все поля сразу
        fields = {
                    "slug": "old_slug",
                    "name": "old_name",
                    "address": "old_address",
                    "latitude": 444444.22334455,
                    "longitude": 444444.22334455,
                    "email": "old_email@mail.ru"
                }
        test_options["student_response"] = self.student_app.patch(
                self.url,
                data=fields,
                content_type="application/json"
            )
        obj = self.check_status_code_jsonify_and_expected(**test_options).json()

        for key, value in fields.items():
            self.assertTrue(
                obj.get(key) == str(value),
                f"Проверьте что при обновлении всех полей по POST-запросу на адрес вида update_view/<id> поле {key} обновилось корректно"
            )
