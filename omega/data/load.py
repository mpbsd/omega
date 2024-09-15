from datetime import date
from omega.data.DATE import DATE, beancount

save_the_date = {
    "registration": {
        "opening": DATE("20240615"),
        "closing": DATE("20240715"),
    },
    "exam": {
        "1": DATE("20240914"),
        "2": DATE("20241005"),
    },
}

today = DATE(date.today().strftime("%Y%m%d"))

payload = {
    "edition": 2024,
    "quota": 10,
    "save_the_date": save_the_date,
    "days_until": {
        "registration": {
            "opening": beancount(
                today,
                save_the_date["registration"]["opening"],
            ),
            "closing": beancount(
                today,
                save_the_date["registration"]["closing"],
            ),
        },
        "exam": {
            "1": beancount(today, save_the_date["exam"]["1"]),
            "2": beancount(today, save_the_date["exam"]["2"]),
        },
    },
}
