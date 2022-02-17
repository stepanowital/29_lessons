import factory
from lookup_queries.models import Store
from django.test import TestCase
from django.test.client import Client
from ttools.skyprotests.tests_mixins import ResponseTestsMixin


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store

    name = "test_store"


TEST_URL_LIST = "/lookup_queries/"


class FkSerializerClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(FkSerializerClassTestCase, cls).setUpClass()
        for _ in range(10):
            StoreFactory.create(name="тестпяттест")
        for _ in range(5):
            StoreFactory.create(name="тесттест")
        for _ in range(5):
            StoreFactory.create(name="ПяТо")

    def setUp(self):
        self.model = Store
        self.student_app = Client()

    def test_url_list_works_correct(self):
        self.url = TEST_URL_LIST
        test_options = {
            "url": self.url,
            "method": "GET",
            "code": [200],
            "student_response": self.student_app.get(self.url),
            "expected": list,
            "django_mode": True,
        }

        response = self.check_status_code_jsonify_and_expected(**test_options)
        self.assertTrue(
            len(response.json()) == 15,
            f"Проверьте что ответ на GET-запрос по адресу {self.url} содержит корректно отфильтрованный список объектов",
        )
        obj = response.json()[0]
        expected_attributes = (field.name for field in self.model._meta.fields)
        self.check_expected_attributes(obj, expected_attributes)

