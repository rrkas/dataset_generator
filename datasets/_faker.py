from datetime import datetime, timedelta
import random
import uuid

from faker import Faker

fake = Faker()


class MyFaker:
    def __init__(self) -> None:
        self.i = 0

    def id(self):
        self.i += 1
        return self.i

    def uuid(self):
        return str(uuid.uuid4())

    def uuid_hex(self):
        return str(uuid.uuid4().hex)

    def first_name(self):
        return fake.first_name()

    def last_name(self):
        return fake.last_name()

    def email(self):
        return random.choice(
            [
                fake.ascii_email,
                fake.ascii_free_email,
                fake.ascii_safe_email,
                fake.company_email,
                fake.free_email,
                fake.email,
                fake.safe_email,
            ]
        )()

    def gender(self):
        return random.choice(
            [
                "Male",
                "Female",
                "Non-binary",
                "Bigender",
                "Agender",
                "Genderfluid",
                "Genderqueer",
                "Polygender",
            ]
        )

    def datetime(self, start_date: datetime, end_date: datetime):
        assert end_date > start_date
        delta = end_date - start_date
        days = delta.days
        random_days = random.randrange(days)
        random_date = start_date + timedelta(days=random_days)
        return random_date

    def designation(self):
        return fake.job()

    def number(self, start: float, end: float, decimal_digits: int = 0):
        assert end > start
        return round(start + ((end - start) * random.random()), decimal_digits)
