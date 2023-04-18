from datetime import datetime, timedelta
from tqdm import tqdm

from ._faker import MyFaker
from ._save import save_to_dir


def store1(limit, format, output_dir):
    """
    dataset name: store1
    Files:
        Customer:
            - id (int)
            - first_name (text)
            - last_name (text)
            - email (text)

        Product:
            - id (int)
            - name (text)
            - price (float)

        Order:
            - id (int)
            - customer_id (int)
            - date (date)

        OrderItem:
            - id (int)
            - order_id (int)
            - product_id (int)
            - quantity (float)

    Possible problem statements:
        1. Get a list of all customers who have made a purchase
        2. Get the total revenue for a particular product
        3. Get a list of the top 10 customers by total revenue
        4. Get a list of all products that have never been purchased
        5. Get the average revenue per order for each month of the year
    """

    customer_limit = limit
    product_limit = max(limit // 20, 50)
    order_limit = max(limit // 20, 50)
    order_item_limit = limit

    fake = MyFaker()
    customers = []
    for _ in tqdm(range(customer_limit)):
        customers.append(
            {
                "id": fake.id(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
            }
        )

    fake = MyFaker()
    products = []
    for _ in tqdm(range(product_limit)):
        products.append(
            {
                "id": fake.id(),
                "name": fake.name(),
                "price": fake.number(1.5, 200.5, 2),
            }
        )

    fake = MyFaker()
    orders = []
    for _ in tqdm(range(order_limit)):
        orders.append(
            {
                "id": fake.id(),
                "customer_id": int(fake.number(1, customer_limit)),
                "date": fake.datetime(
                    start_date=datetime.utcnow() - timedelta(days=365),
                    end_date=datetime.utcnow(),
                ).isoformat(),
            }
        )

    fake = MyFaker()
    order_items = []
    for _ in tqdm(range(order_item_limit)):
        order_items.append(
            {
                "id": fake.id(),
                "order_id": int(fake.number(1, order_limit)),
                "product_id": int(fake.number(1, product_limit)),
                "quantity": fake.number(1, 100, 2),
            }
        )

    save_to_dir(
        {
            "Customer": customers,
            "Product": products,
            "Order": orders,
            "OrderItem": order_items,
        },
        format,
        output_dir,
    )
