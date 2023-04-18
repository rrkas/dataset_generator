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
    inventory_limit = limit

    fake = MyFaker()
    inventory = []
    for _ in tqdm(range(inventory_limit)):
        inventory.append(
            {
                "id": fake.id(),
                "material": fake.material_name(),
                "qty_kg": fake.number(0.2, 1425.5, 1),
                "density_gcm": fake.number(0.01, 3.5, 3),
                "rate_g": fake.number(0.01, 2500.25, 3),
            }
        )

    save_to_dir(
        {"Inventory": inventory},
        format,
        output_dir,
    )


def inventory2(limit, format, output_dir):
    """
    dataset name: inventory2
    Files:
        Seller:
            - id (int)
            - name (text)
        Inventory:
            - id (int)
            - seller_id (int)
            - name (text)
            - batch (uuid)
            - quantity (int)
            - rate (float)

    Possible problem statements:
        1. Total value of inventory
        2. Seller wise total value of inventory
        3. Batch wise total value of inventory
        4. Inventory count by rate buckets (0-10, 10-20, ...)
    """
    seller_limit = max(limit // 20, 50)
    inventory_limit = limit

    fake = MyFaker()
    sellers = []
    for _ in tqdm(range(seller_limit)):
        sellers.append({"id": fake.id(), "name": fake.name()})

    fake = MyFaker()
    inventory = []
    for _ in tqdm(range(inventory_limit)):
        inventory.append(
            {
                "id": fake.id(),
                "seller_id": int(fake.number(1, seller_limit)),
                "material": fake.material_name(),
                "qty_kg": fake.number(0.2, 1425.5, 1),
                "density_gcm": fake.number(0.01, 3.5, 3),
                "rate_g": fake.number(0.01, 2500.25, 3),
            }
        )

    save_to_dir(
        {
            "Seller": sellers,
            "Inventory": inventory,
        },
        format,
        output_dir,
    )
