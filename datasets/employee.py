from datetime import datetime, timedelta

from ._faker import MyFaker


def employee1(fake: MyFaker):
    """
    Employee Dataset 1:
    Fields:
        id
        first_name
        last_name
        email
        gender
    """
    return {
        "id": fake.id(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "gender": fake.gender(),
        "dob": fake.datetime(
            start_date=datetime.utcnow() - timedelta(days=365 * 40),
            end_date=datetime.utcnow(),
        ).isoformat()
        + "Z",
        "designation": fake.designation(),
        "monthly_salary": fake.number(20000, 150000, 2),
    }
