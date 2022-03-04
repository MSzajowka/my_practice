from datetime import datetime, timedelta


def tomorrow():
    return datetime.today() + timedelta(1)


print(tomorrow())
