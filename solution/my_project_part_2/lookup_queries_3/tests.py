import factory
from lookup_queries_3.models import Store
from django.test import TestCase
from django.test.client import Client
from ttools.skyprotests.tests_mixins import ResponseTestsMixin


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store

    name = "test_store"
    close_hour = 22


TEST_URL_LIST = "/lookup_queries_3/"


class FkSerializerClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(FkSerializerClassTestCase, cls).setUpClass()
        for _ in range(3):
            StoreFactory.create(open_hour=8)
        for _ in range(7):
            StoreFactory.create(open_hour=9)
        for _ in range(5):
            StoreFactory.create(open_hour=10)
        for _ in range(5):
            StoreFactory.create(open_hour=11)
        for _ in range(5):
            StoreFactory.create(open_hour=12)

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

