from datetime import datetime, timedelta

from tqdm import tqdm

from ._faker import MyFaker
from ._save import save_to_dir


def expense1(limit, format, output_dir):
    """
    dataset name: expense1
    Files:
        Expense:
            - id (int)
            - user_id (text)
            - category (text)
            - description (text)
            - date (date)
            - value (float)

    Possible problem statements:
        1. User wise total expense
        2. User wise annual expense
        3. User wise average expense
        4. User wise category wise total expense
        5. User wise category wise annual expense
        6. User wise category wise average expense
        7. Category wise total expense
        8. Category wise annual expense
        9. Category wise average expense
        10. Total expense
        11. Annual expense
        12. Average expense
    """
    fake = MyFaker()
    expenses = []
    for _ in tqdm(range(limit)):
        expenses.append(
            {
                "id": fake.id(),
                "user_id": f"user_{int(fake.number(1, 50))}",
                "category": fake.material_name(),
                "description": fake.description(),
                "date": fake.datetime(
                    start_date=datetime.utcnow() - timedelta(days=365 * 40),
                    end_date=datetime.utcnow(),
                ).isoformat(),
                "value": fake.number(10, 50000, 2),
            }
        )

    save_to_dir(
        {"Expense": expenses},
        format,
        output_dir,
    )
