from datetime import datetime, timedelta
from tqdm import tqdm

from ._faker import MyFaker
from ._save import save_to_dir


def employee1(limit, format, output_dir):
    """
    dataset name: employee1
    Files:
        Employee:
            - emp_id (int)
            - first_name (text)
            - last_name (text)
            - email (text)
            - gender (text)
            - dob (date)
            - designation (text)
            - monthly_salary (float)

    Possible problem statements:
        1. Designation wise user count
        2. Age wise user count
        3. Gender wise user count
        4. Total salary paid by the company per month and per year
        5. Salary bracket wise user count (range of 10000)
    """

    fake = MyFaker()
    data = []
    for _ in tqdm(range(limit)):
        data.append(
            {
                "emp_id": fake.id(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "gender": fake.gender(),
                "dob": fake.datetime(
                    start_date=datetime.utcnow() - timedelta(days=365 * 40),
                    end_date=datetime.utcnow(),
                ).isoformat(),
                "designation": fake.designation(),
                "monthly_salary": fake.number(20000, 150000, 2),
            }
        )

    save_to_dir(data, format, output_dir, "Employee")
