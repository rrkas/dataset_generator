from . import employee, store, inventory, expense


def generate_data(
    dataset_name: str,
    limit: int,
    format: str,
    output_dir: str,
):
    datasets = [
        employee.employee1,
        employee.employee2,
        store.store1,
        inventory.inventory1,
        inventory.inventory2,
        expense.expense1,
    ]

    dataset = {dataset.__name__: dataset for dataset in datasets}[dataset_name]

    # generate data
    dataset(limit, format, output_dir)

    return dataset
