from datetime import datetime, timedelta

from ._faker import MyFaker


def employee1(fake: MyFaker):
    """
    employee1:
        emp_id              - integer
        first_name          - string
        last_name           - string
        email               - string
        gender              - string
        dob                 - date-time in ISO format (string)
        designation         - string
        monthly_salary      - float (2 decimal places)

    Possible problem statements:
        1. Designation wise user count
        2. Age wise user count
        3. Gender wise user count
        4. Total salary paid by the company per month and per year
        5. Salary bracket wise user count (range of 10000)

    """
    return {
        "emp_id": fake.id(),
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
