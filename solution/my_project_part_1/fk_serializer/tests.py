import factory
from fk_serializer.models import Store, City
from django.test import TestCase
from django.test.client import Client
from ttools.skyprotests.tests_mixins import ResponseTestsMixin


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = "test city"


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store

    slug = "testmarket"
    name = "teststore"
    address = "Тестовая"
    latitude = 777777.39503894
    longitude = 777777.5573879
    email = "test_sky@pro.com"
    city = 1


TEST_URL = "/fk_serializer/"


class FkSerializerClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(FkSerializerClassTestCase, cls).setUpClass()
        for _ in range(10):
            CityFactory.create()
        for i in range(10):
            city = City.objects.get(id=i+1)
            StoreFactory.create(city=city)

    def setUp(self):
        self.model = Store
        self.student_app = Client()

    def test_url_works_correct(self):
        self.url = TEST_URL
        test_options = {
            "url": self.url,
            "method": "GET",
            "code": [200],
            "student_response": self.student_app.get(self.url),
            "expected": list,
            "django_mode": True,
        }

        response = self.check_status_code_jsonify_and_expected(**test_options)
        db_count = Store.objects.all().count()
        self.assertTrue(
            len(response.json()) == db_count,
            f"Проверьте что ответ на GET-запрос по адресу {self.url} возвращается список объектов из БД",
        )
        obj = response.json()[0]
        expected_attributes = (field.name for field in self.model._meta.fields)
        self.check_expected_attributes(obj, expected_attributes)

        # проверяем поле city:
        self.assertTrue(
            obj.get("city") == {"id": 1, "name": "test city"},
            "Проверьте, что поле city представляет собой вложенный словарь, с полями id и name"
        )
