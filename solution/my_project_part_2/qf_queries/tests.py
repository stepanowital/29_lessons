import factory
from qf_queries.models import Store
from django.test import TestCase
from django.test.client import Client
from ttools.skyprotests.tests_mixins import ResponseTestsMixin


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store

    name = "test_store"
    open_hour = 10
    close_hour = 22


TEST_URL_LIST = "/qf_queries/"


class FkSerializerClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(FkSerializerClassTestCase, cls).setUpClass()
        for _ in range(3):
            StoreFactory.create(email="testivan@skypro.ru")
        for _ in range(7):
            StoreFactory.create(director="ivan")
        for _ in range(5):
            StoreFactory.create(director="test_ivan")
        for _ in range(5):
            StoreFactory.create(email="testskypro@skypro.ru")
        for _ in range(5):
            StoreFactory.create(director="longtest")

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

