import datetime
from json import JSONEncoder

from requests import get, post, delete, put

base_url = "http://127.0.0.1:5000"


class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


def test_post() -> None:
    global base_url
    print("Работа post запроса.")
    url = base_url + "/change_blog"
    answer = post(url, json={"pharmacy_id": 0,
                             "pharmacy_name": "Новая аптека Аптека",
                             "patients_full_name": "Артем Сергеевич",
                             "name_of_medicine": "Милом",
                             "type_of_medicine": "Д",
                             "price_of_medicine": 2500,
                             "county_of_origin": "RU",
                             "date_of_sale": datetime.date(2021, 10, 2)})
    if answer.ok:
        print(answer.text)
    input()


def test_get() -> None:
    global base_url
    print("Работа get запроса.")
    url = base_url + "/get_pharmacies"
    answer = get(url)
    if answer.ok:
        print(answer.text)
    input()


def test_delete() -> None:
    global base_url
    print("Работа delete запроса.")
    url = base_url + "/delete_blog"
    answer = delete(url, json={"pharmacy_id": 0})
    if answer.ok:
        print(answer.text)


def test_put() -> None:
    global base_url
    print("Работа put запроса.")
    url = base_url + "/change_blog"
    answer = put(url, json={"pharmacy_id": 0,
                            "pharmacy_name": "Обновленная Аптека",
                            "patients_full_name": "Николай Сергеевич",
                            "name_of_medicine": "Киромол",
                            "type_of_medicine": "В",
                            "price_of_medicine": 1249,
                            "county_of_origin": "RU",
                            "date_of_sale": datetime.date(2020, 10, 2)})
    if answer.ok:
        print(answer.text)
    input()


def main() -> None:
    test_get()
    test_delete()
    test_post()
    test_put()


if __name__ == "__main__":
    main()
