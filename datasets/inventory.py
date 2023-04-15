from datetime import datetime, timedelta

from tqdm import tqdm

from ._faker import MyFaker
from ._save import save_to_dir


def inventory1(limit, format, output_dir):
    """
    dataset name: inventory1
    Files:
        Inventory:
            - id (int)
            - material (text)
            - qty_kg (float)
            - density_gcm (float) (g/ cu. cm)
            - rate_g (float)

    Possible problem statements:
        1. Material wise total quantity
        2. Material wise total space occupied (cu. m)
        3. Material wise total value
    """
    fake = MyFaker()
    depts = []
    for _ in tqdm(range(limit)):
        depts.append(
            {
                "id": fake.id(),
                "material": fake.material_name(),
                "qty_kg": fake.number(0.2, 1425.5, 1),
                "density_gcm": fake.number(0.01, 3.5, 3),
                "rate_g": fake.number(0.01, 2500.25, 3),
            }
        )
    save_to_dir(depts, format, output_dir, "Inventory")
