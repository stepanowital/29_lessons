# Урок 29
Для начала работы скопируйте репозиторий на локальную машину с помощью команды в терминале:

`git clone https://github.com/skypro-008/lesson29-and-tests.git`

Откройте с клонированный репозиторий в PyCharm.

### Создайте виртуальное окружение:

#### Простой вариант:
Pycharm может предложить вам сделать это после того, как вы откроете папку с проектом.
В этом случае после открытия папки с проектом в PyCharm.
Появляется всплывающее окно, Creating virtual environment c тремя полями.
В первом поле выбираем размещение папки с виртуальным окружением, как правило, это папка venv
в корне проекта
Во втором поле выбираем устанавливаемый интерпретатор по умолчанию (можно оставить без изменений)
В 3 поле выбираем список зависимостей (должен быть выбран файл requirements.txt, 
находящийся в корне папки проекта)

#### Если этого не произошло, тогда следует выполнить следующие действия вручную:
#### Установка виртуального окружения:
1. Во вкладке File выберите пункт Settings
2. В открывшемся окне, с левой стороны найдите вкладку с именем
вашего репозитория (Project: lesson29-and-tests)
3. В выбранной вкладке откройте настройку Python Interpreter
4. В открывшейся настройке кликните на значок ⚙ (шестеренки) 
расположенный сверху справа и выберите опцию Add
5. В открывшемся окне слева выберите Virtualenv Environment, 
а справа выберите New Environment и нажмите ОК

#### Установка зависимостей:
Для этого можно воспользоваться графическим интерфейсом PyCharm,
который вам предложит сделать это как только вы откроете файл с заданием.

Или же вы можете сделать это вручную, выполнив следующую команду в терминале:
`pip install -r requirements.txt`

*У владельцев операционной системы MacOS могут возниктут сложности с установкой зависимостей.
Если возникла ошибка - сначала выполните в терминале команду brew install postgresql.
После её выполнения ошибок с установкой зависимостей быть не должно.
#### Настройка виртуального окружения завершена!
### Подготовка проекта django
После того как Вы установили все зависимости, необходимо подготовить django к работе:
для этого нам потребуется:

1. Иметь возможность запуска на локальной машине docker-контейнера 
(необходимо для запуска контейнера с базы данных):
- переходим в каталог `postgres_l29` и выполняем команду `docker-compose up`.

2. Выполнить необходимые команды для подготовки базы данных к работе:
Текущий проект уже содержит настроенную базу данных, но пока еще она 
пустая, не содержит таблиц, а всё её наполнение
находится в фикстурах (в django - файлы в формате json содержащие данные для наполнения БД).

Для начала нужно создать необходимые таблицы в базе данных с помощью команды:
python3 manage.py migrate (находясь в папке `my_project_part_1`)
а затем выполнить команду `python3 manage.py loadall` из этой же директории
   (для загрузки всех объектов в базу данных).
Уточним, что loadall является кастомной командой которая представляет
собой несколько идущих подряд команд
`python3 manage.py loaddata file.json` где file.json - файл с данными для БД
Если команда выполнена успешна вы увидите следующий текст:
```
Installed 2 object(s) from 1 fixture(s)
Installed 6 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 1 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 11 object(s) from 1 fixture(s)
```
После того как все подготовительные мероприятия выполнены - можно приступать к работе.

Первое, что необходимо сделать - изучить представленный проект.
Здесь одно Джанго-приложение соответствует одному заданию тренажера
ознакомится с адресами приложений можно всё также в файле `my_project/urls.py`
*Обратите внимание, что часть адресов, представленных в заданиях ниже уже реализованы
и здесь Вам требуется только дополнить их соответствующим образом.*


### Порядок выполнения заданий

## Часть 1. my_project_part_1

### Задание list_view
Перейдите в приложение list_view.
Напишите эндпоинт, который будет возвращать список всех объектов из базы данных
в ответ на GET-запрос по адресу `/list_view/`.
Каждый элемент списка должен содержать все поля модели
При подготовке эндпоинта используйте generic-классы.

### Задание retrieve_view
Перейдите в приложение retrieve_view.
Напишите эндпоинт, который в ответ на GET-запрос по адресу `/retrieve_view/{id}/` 
по переданному id будет возвращать словарь, содержащий все поля модели из БД.
При подготовке эндпоинта используйте generic-классы.

### Задание slug_retrieve_view
Перейдите в приложение slug_retrieve_view.
Напишите эндпоинт, который в ответ на GET-запрос по адресу `/slug_retrieve_view/{slug}/` 
по переданному slug будет возвращать словарь, содержащий все поля модели из БД.
При подготовке эндпоинта используйте generic-классы.

### Задание update_view
Перейдите в приложение slug_retrieve_view.
Напишите эндпоинт, который в ответ на POST-запрос по адресу `/update_view/{id}/`
с информацией json вида:
по переданному id будет обновлять любое из полей и, в последствии, возвращать все поля модели.
Например при передаче следующих данных:
```json
{
   "name": "new_name",
   "email": "new_email@expample.com"
}
```
должны быть обновлены поля name и email
При подготовке эндпоинта используйте generic-классы.

### Задание simple_serializer
Перейдите в приложение simple_serializer
и напишите сериалайзер для модели Store текущего приложения.
Например, при GET - запросе на адрес `/simple_serializer/` должен возвращаться **_список_**
из объектов следующего вида:
```json
    {
        "id": 1,
        "slug": "skymarket",
        "name": "Самый лучший магазин",
        "address": "Солнцевская, д.5",
        "latitude": "349938.395039",
        "longitude": "664762.557388",
        "email": "sky@pro.com"
    }
```

### Задание fk_serializer
Перейдите в приложение fk_serializer
и напишите необходимые сериалайзеры для модели Store текущего приложения.
Например, при GET - запросе на адрес `/fk_serializer/` должен возвращаться **_список_**
из объектов следующего вида:
```json
{
        "id": 1,
        "city": {
            "id": 1,
            "name": "Сочи"
        },
        "slug": "skymarket",
        "name": "Самый лучший магазин",
        "address": "Солнцевская, д.5",
        "latitude": "349938.395039",
        "longitude": "664762.557388",
        "email": "sky@pro.com"
    }
```

### Задание m2m_serializer
Перейдите в приложение m2m_serializer
и напишите необходимые сериалайзеры для модели Store текущего приложения.
Например, при GET - запросе на адрес `/m2m_serializer/` должен возвращаться **_список_**
из объектов следующего вида:
```json
{
        "id": 1,
        "city": {
            "id": 1,
            "name": "Сочи"
        },
        "work_hours": [
            {
                "id": 1,
                "week_day": 0,
                "open_time": "10:00:00",
                "close_time": "22:00:00"
            },
            {
                "id": 2,
                "week_day": 1,
                "open_time": "10:00:00",
                "close_time": "22:00:00"
            }
        ],
        "slug": "skymarket",
        "name": "Самый лучший магазин",
        "address": "Солнцевская, д.5",
        "latitude": "349938.395039",
        "longitude": "664762.557388",
        "email": "sky@pro.com"
    }
```


## Часть 2 my_project_part_2
Перед началом работы не забудьте подготовить проект Django

### Задание router
Перейдите в приложение router и
используя `SimpleRouter` из стандартных средств DRF,
опишите в urls.py маршрутизацию так, чтобы работали следующие эндпоинты: 
`router_stores/` - возвращает список магазинов
`router_stores/1/` - возвращает магазин по переданному ID


### Задание lookup_queries
Перейдите в приложение lookup_queries и
допишите представленный класс в файле views.py так,
чтобы при обращении на адрес
`lookup_queries/` - возвращался только список магазинов, 
содержащих в своем имени (name) текст `пят`, без учета регистра.
Также не забудьте настроить файл urls.py внутри приложения
Ответ должен содержать все поля модели.

### Задание lookup_queries_2
Перейдите в приложение lookup_queries_2 и
допишите представленный класс в файле views.py так,
чтобы при обращении на адрес
`lookup_queries_2/` - возвращался только список магазинов, 
адрес у которых заканчивается на `д. 30`.
Ответ должен содержать все поля модели.

### Задание lookup_queries_3
Перейдите в приложение lookup_queries_3 и
допишите представленный класс в файле views.py так,
чтобы при обращении на адрес
`lookup_queries_3/` - возвращался только список магазинов, 
адрес у которых время открытия (open_hour) попадает в диапазон от 8 до 10 часов.
Ответ должен содержать все поля модели.

### Задание qf_queries
Перейдите в приложение qf_queries и
допишите запрос так, чтобы 
при GET-запросе на адрес `/qf_queries/` 
он отдавал все записи, в которых есть строка ivan в полях email или name.


### Задание fk_search
Перейдите в приложение fk_search и
допишите представленный класс в файле views.py так,
чтобы при обращении на адрес
`fk_search/` - возвращался только список магазинов, 
расположенных в Самаре.
Ответ должен содержать все поля модели.

### Задание delete_if_null
Перейдите в приложение delete_if_null и
допишите представленный класс в файле views.py так,
чтобы при обращении на адрес
`delete_if_null/` - из базы данных удалялись магазины, у которых
число посещений равняется нулю (visits=0).
Ответ должен содержать все поля модели.

Проверить все задания проекта вы можете с помощью команды `python3 manage.py test`
Проверить только одно задание проекта можно с помощью команды `python3 manage.py test <app>`