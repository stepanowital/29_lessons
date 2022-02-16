import inspect
import json
import sqlite3
import unittest
from unittest import TestCase

import marshmallow
import sqlalchemy
from bs4 import BeautifulSoup


class DataBaseTestsMixin:
    """
    Includes methods for Tests with DB Models and Queries
    """

    STRING = "String"
    INTEGER = "Integer"
    DATE = "Date"

    def get_query_info(self, query):
        from_sql_checker = self._sql_checker(query)
        from_cursor = self._get_cursor_info(query)
        return {"query_info": from_sql_checker, "cursor_info": from_cursor}

    def _get_db_cursor(self, query):
        con = sqlite3.connect("../netflix.db")
        cur = con.cursor()
        cur.execute(query)
        return cur

    def _get_cursor_info(self, query):
        """
        Creates dict with info from SQL query string
        """
        cur = self._get_db_cursor(query)
        return self.get_cursor_info(cur)

    def get_cursor_info(self, cursor):
        """
        Returns dict with info about current cursor with query
        """
        columns = cursor.description
        columns_len = len(columns)
        names_of_columns = []
        query_result = cursor.fetchall()
        rows_count = len(query_result)
        for name in columns:
            names_of_columns.append(name[0])
        return {
            "columns": names_of_columns,
            "columns_count": columns_len,
            "query_result": query_result,
            "rows_count": rows_count,
        }

    def _sql_checker(self, query: str):
        """
        returns blocks with SQL keyword
        and keyword value
        """
        query = query.lower()
        keywords = self._get_key_words(query)
        select_ind = query.find("select ")
        from_ind = query.find("from ")
        where_ind = query.find("where ")
        and_ind = query.find(" and ")
        select_block = query[select_ind:from_ind]
        from_block = query[from_ind:where_ind]
        where_block = query[where_ind:]
        and_block = None
        if and_ind:
            where_block = query[where_ind:and_ind]
            and_block = query[and_ind:]
        blocks = {
            "колонка": select_block,
            "таблица": from_block,
            "условие": where_block,
            "доп условие": and_block,
        }
        for key, value in blocks.items():
            blocks[key] = self._cleaner(blocks[key])
        blocks["keywords"] = keywords
        return blocks

    def _cleaner(self, lst):
        lst = lst.split(" ")
        key_words = ["select", "from", "where", "like", "distinct", "and", ""]
        for value in key_words:
            if value in lst:
                lst.remove(value)
        for value in lst:
            if "," in value:
                devided_value = value.split(",")
                try:
                    devided_value.remove("")
                except:  # noqa: E722
                    pass
                lst.remove(value)
                lst += devided_value
        return lst

    def _get_key_words(self, query):
        keywords = [
            "select",
            "from",
            "where",
            "like",
            "group by",
            "distinct",
            "limit",
            "order by",
        ]
        lst = []
        for keyword in keywords:
            if keyword in query:
                lst.append(keyword)
        return lst

    def field_name_checker(self, student_columns, author_columns):
        self.assertEqual(
            student_columns,
            author_columns,
            (
                r"%@Проверьте, что правильно определили "
                "поля модели Author. "
                f"Вы выбрали {student_columns}, тогда "
                f"как необходимо {author_columns}"
            ),
        )

    def field_type_checker(
        self, module=None, model_name: str = None, type_name: str = None, fields=None
    ):  # field.name (field.name, field.name)
        correct_field_type = getattr(sqlalchemy, type_name)
        model = getattr(module, model_name)
        fields = (getattr(model, field_name) for field_name in fields)
        for field in fields:
            name = field.property.key
            self.assertTrue(
                isinstance(field.type, correct_field_type),
                f"%@Проверьте имеет ли поле {name} модели {model_name} "
                f"тип {type_name}",
            )

    def django_field_checker(self, current_fields, expected_fields, field_type):
        for attribute in expected_fields:
            expected_field = expected_fields.get(attribute)
            field = current_fields.get(attribute)
            self.assertIsInstance(
                field,
                field_type,
                f"Проверьте, что у поля {field.name} правильно указан тип поля",
            )
            if expected_field:
                for attribute in expected_field:
                    self.assertTrue(
                        getattr(field, attribute) == expected_field.get(attribute),
                        f"Проверьте, что у поля {field.name} правильно указано свойство {attribute}",
                    )

    def django_foreign_key_field_checker(
        self, foreign_key_field, expected_field, field_type
    ):
        self.assertIsInstance(
            foreign_key_field,
            field_type,
            f"Проверьте, что у поля {foreign_key_field.name} правильно указан тип поля",
        )

        # check model target:
        target_model = expected_field.get("model")
        self.assertTrue(
            foreign_key_field.related_model == target_model,
            f"%@Проверьте что поле {foreign_key_field.name} ссылается на правильную модель",
        )

        # check on_delete method
        expected_on_delete_func = expected_field.get("on_delete")
        self.assertTrue(
            foreign_key_field.remote_field.on_delete == expected_on_delete_func,
            "%@Проверьте, что у Вас верно присвоен аттрибут on_delete для поля foreign_key_field.name",
        )

    def django_foreign_key_field_checker(
        self, foreign_key_field, expected_field, field_type
    ):
        self.assertIsInstance(
            foreign_key_field,
            field_type,
            f"Проверьте, что у поля {foreign_key_field.name} правильно указан тип поля",
        )

        # check model target:
        target_model = expected_field.get("model")
        self.assertTrue(
            foreign_key_field.related_model == target_model,
            f"%@Проверьте что поле {foreign_key_field.name} ссылается на правильную модель",
        )

        # check on_delete method
        expected_on_delete_func = expected_field.get("on_delete")
        self.assertTrue(
            foreign_key_field.remote_field.on_delete == expected_on_delete_func,
            "%@Проверьте, что у Вас верно присвоен аттрибут on_delete для поля foreign_key_field.name",
        )


class ResponseTestsMixin:
    def _required_args_checker(self: TestCase, *args, **kwargs):
        """
        for usage in module.
        Checks that all arguments in functions is defined
        required arguments can be added to this func as string
        and as list
        if arg is list checks that any of list element is in required
        """
        for test_arg in args:  # required args
            if isinstance(test_arg, list):
                if not {*test_arg}.intersection({*kwargs.keys()}):
                    raise ValueError(
                        f"key argument '{test_arg}' must be defined."
                        f"look at testMethod= here:{self.__eq__}"
                    )
            elif not kwargs.get(test_arg):
                raise ValueError(
                    f"key argument '{test_arg}' must be defined."
                    f"look at testMethod= here:{self.__eq__}"
                )

    def check_status_code_jsonify_and_expected(self: unittest.TestCase, **kwargs):
        """
        compex check that testing:
        - response status code
        - is_json type
        - optional expected_obj (if arg expected is not None)
        - optional answer_obj - check what's returned
        """
        code: list = kwargs.get("code")
        url: str = kwargs.get("url")
        response = kwargs.get("response") or kwargs.get("student_response")
        expected: object = kwargs.get("expected")
        method: str = kwargs.get("method")
        answer = kwargs.get("answer")
        django_mode = kwargs.get("django_mode", False)
        debug_mode = kwargs.get("debug_mode", False)
        if debug_mode:
            return response
        additional_text_on_code_test = kwargs.get("text")
        if additional_text_on_code_test is None:
            additional_text_on_code_test = ""
        self._required_args_checker(
            "url", ["response", "student_response"], "method", **kwargs
        )
        if code not in [404, 500]:
            self.assertIn(
                response.status_code,
                code,
                (
                    f"%@Проверьте, что {additional_text_on_code_test} адрес"
                    f" {url} доступен, а {method}-запрос "
                    f"возвращает код {code}"
                ),
            )
        else:
            self.assertIn(
                response.status_code,
                [404, 500],
                (
                    f"Проверьте, что при запросе на {url} "
                    "(в случае отсутствия объекта или обращении на несуществующую страницу)"
                    "возвращается ошибка 404"
                ),
            )
            return response
        # self.assertTrue(  # json_fix
        #     response.is_json,
        #     (f"%@Проверьте, что в ответ на {method}-запрос "
        #      f"по адресу {url} возращает данные в формате json."
        #      " Попробуйте использовать функцию jsonify из библиотеки flask."))
        if expected:
            if django_mode:
                expected_json = response.json()
            else:
                expected_json = response.json or json.loads(response.data)  # json_fix
            self.assertFalse(
                expected_json == {},
                (
                    f"%@Проверьте что в ответ на {method}-запрос по адресу {url} "
                    f"возвращается не пустой ответ"
                ),
            )
            self.assertTrue(
                isinstance(expected_json, expected),
                f"%@Проверьте что в ответ на {method}-запрос по адресу {url}"
                f" возвращается {expected}",
            )
        if answer:
            answer_json = response.json or json.loads(response.data)  #
            self.assertTrue(
                answer == answer_json,
                f"%@Проверьте, что в ответе на {method}-запрос по адресу {url}"
                f" возвращается корректный ответ",
            )
        return response

    def compare_result_fields_with_author_solution(self, many=False, **kwargs):
        """
        Compare student response.data with author sulution.
        - Note:* (response.data must be not None)
        - Use `many=true` for inspecting response.data which contains list
        """
        self._required_args_checker(
            "method", "url", "student_response", "author_response", **kwargs
        )
        method = kwargs.get("method")
        url = kwargs.get("url")
        student_response = kwargs.get("student_response")
        student_response = student_response.json or json.loads(
            student_response.data
        )  # json_fix
        author_response = kwargs.get("author_response").json
        if author_response == "":
            raise ValueError(
                "In this Case response returns None"
                " so no one field can be checked, "
                "delete this function from testCase"
            )
        if many:
            author_data = author_response[0]
            data = student_response[0]
        else:
            author_data = author_response
            data = student_response
        if (
            author_data == data == []  # Ecли ответ будет пустым тогда
            or author_data == data == {}
        ):  # поля не проверять
            return  # заканчиваем проверку здесь
        if not many and isinstance(author_response, list):
            raise ValueError(
                "check `response.data` maybe many" " arg must have True value"
            )
        if not many:
            self.assertFalse(
                isinstance(student_response, list),
                (
                    f"%@Проверьте, что при {method}-запросе на адрес {url} "
                    f"ответ возвращается {dict}"
                ),
            )
        student_keys = data.keys()
        for key, value in author_data.items():
            self.assertIn(
                key,
                student_keys,
                f"%@ Проверьте, что ответ на {method}-запрос по адресу {url} "
                f"содержит поле {key}",
            )
            self.assertEqual(
                value,
                data[key],
                f"%@ Проверьте, что ответ на {method}-запрос по адресу {url} "
                f"в поле {key} содержится правильное значение",
            )

    def check_expected_attributes(self, obj, expected_attributes):
        for attribute in expected_attributes:
            self.assertIn(
                attribute,
                obj,
                f"Проверьте, что ответ на GET-запрос по адресу {self.url} "
                f"возвращает объекты, которые содержат в себе поле {attribute}",
            )

    def check_unexpected_attributes(self, obj, unexpected_attributes):
        for attribute in unexpected_attributes:
            self.assertNotIn(
                attribute,
                obj,
                f"Проверьте, что ответ на GET-запрос по адресу {self.url} "
                f"возвращаются поля в соответствии со спецификацией - {attribute} является лишним",
            )


class SchemaTestsMixin(ResponseTestsMixin):
    def schema_is_valid(self, **kwargs):
        """
        Simple test that Schema is valid:
        - Schema exists
        - Schema is class
        - Schema is class of marshmallow.Schema
        """
        self._required_args_checker("main", "schema_name", **kwargs)
        main = kwargs.get("main")
        schema_name = kwargs.get("schema_name")
        self.assertTrue(
            hasattr(main, schema_name),
            f"%@Проверьте, что класс {schema_name} определен" " в модуле",
        )
        student_schema = getattr(main, schema_name)
        self.assertTrue(
            inspect.isclass(student_schema),
            f"%@Проверьте, что {student_schema} это класс",
        )
        self.assertTrue(
            issubclass(student_schema, marshmallow.Schema),
            (
                "%@Проверьте, правильно ли указан родительский класс у "
                f"класса {student_schema}"
            ),
        )

    def compare_schema_with_author_solution(self, **kwargs):
        """
        Compare field names and types
        between author and student solutions
        """
        self._required_args_checker("student_schema", "author_schema", **kwargs)
        author_schema = kwargs.get("author_schema")
        author_fields_dict = author_schema._declared_fields
        student_schema = kwargs.get("student_schema")
        student_fields_dict = student_schema._declared_fields
        student_fields = student_fields_dict.keys()
        # compare fields and their types
        for field, type in author_fields_dict.items():
            self.assertIn(
                field,
                student_fields,
                (f"%@Проверьте, что схема {student_schema}" f" содержит поле {field}"),
            )
            self.assertTrue(
                isinstance(student_fields_dict[field], type.__class__),
                f"%@Проверьте, что правильно определён тип "
                f"у поля {field} схемы {student_schema}."
                f"Попробуйте использовать {type.__class__}",
            )


class TemplateMixin(ResponseTestsMixin):
    def check_code_and_get_soup(self, url, code):
        response = self.app.get(url)
        self.assertTrue(
            response.status_code == code,
            f"%@Проверьте, что адрес 127.0.0.1:5000'{url}' доступен из браузера",
        )

        soup = BeautifulSoup(response.get_data(True), "html.parser")
        return soup


class AnnotationsCheckMixin:
    def check_annotations(self, student_class, author_class):
        student_annotations = student_class.__annotations__
        author_annotations = author_class.__annotations__

        for annotation in author_annotations:
            self.assertIn(
                annotation,
                student_annotations,
                f"%@Проверьте что написали аннотацию для аргумента {annotation}",
            )

        for annotation in author_annotations:
            self.assertEqual(
                student_annotations.get(annotation),
                author_annotations.get(annotation),
                f"%@Проверьте что в классе {student_class.__name__} правильно указана аннотация для аргумента {annotation}",
            )
