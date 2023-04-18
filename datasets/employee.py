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
    employee_limit = limit

    fake = MyFaker()
    data = []
    for _ in tqdm(range(employee_limit)):
        data.append(
            {
                "emp_id": fake.id(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "gender": fake.gender(),
                "dob": fake.datetime(
                    start_date=datetime.utcnow() - timedelta(days=365 * 40),
                    end_date=datetime.utcnow() - timedelta(days=365 * 20),
                ).isoformat(),
                "designation": fake.designation(),
                "monthly_salary": fake.number(20000, 150000, 2),
            }
        )

    save_to_dir({"Employee": data}, format, output_dir)


def employee2(limit, format, output_dir):
    """
    dataset name: employee2
    Files:
        Employee:
            - employee_id (int)
            - first_name (text)
            - last_name (text)
            - birth_date (date)
            - hire_date (date)
            - job_title (text)
            - department_id (int)

        Department:
            - department_id (int)
            - department_name (text)

        Salary:
            - transaction_id (int)
            - employee_id (int)
            - salary (float)
            - from_date (date)
            - to_date (date)

    Possible problem statements:
        1. Get the average salary by department
        2. Get the top 10 highest paid employees
        3. Get the number of employees hired in each year
        4. Get the average salary by job title
        5. Get the departments with the highest and lowest average salaries
    """

    employee_limit = limit
    dept_limit = max(limit // 20, 50)
    salary_limit = limit

    fake = MyFaker()
    employees = []
    for _ in tqdm(range(employee_limit)):
        employees.append(
            {
                "employee_id": fake.id(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "birth_date": fake.datetime(
                    start_date=datetime.utcnow() - timedelta(days=365 * 40),
                    end_date=datetime.utcnow() - timedelta(days=365 * 20),
                ).isoformat(),
                "hire_date": fake.datetime(
                    start_date=datetime.utcnow() - timedelta(days=365 * 10),
                    end_date=datetime.utcnow() - timedelta(days=365),
                ).isoformat(),
                "job_title": fake.designation(),
                "department_id": int(fake.number(1, dept_limit)),
            }
        )

    fake = MyFaker()
    depts = []
    for _ in tqdm(range(dept_limit)):
        depts.append(
            {
                "department_id": fake.id(),
                "department_name": fake.first_name(),
            }
        )

    fake = MyFaker()
    salaries = []
    for _ in tqdm(range(salary_limit)):
        from_date = fake.datetime(
            start_date=datetime.utcnow() - timedelta(days=365 * 4),
            end_date=datetime.utcnow() - timedelta(days=60),
        )
        to_date = fake.datetime(
            start_date=from_date,
            end_date=from_date + timedelta(days=360),
        )
        salaries.append(
            {
                "transaction_id": fake.id(),
                "employee_id": int(fake.number(1, employee_limit)),
                "salary": int(fake.number(20000, 130000)),
                "from_date": from_date.isoformat(),
                "to_date": to_date.isoformat(),
            }
        )

    save_to_dir(
        {
            "Employee": employees,
            "Department": depts,
            "Salary": salaries,
        },
        format,
        output_dir,
    )
