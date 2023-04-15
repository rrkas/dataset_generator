from . import employee, store


def generate_data(
    dataset_name: str,
    limit: int,
    format: str,
    output_dir: str,
):
    datasets = [
        employee.employee1,
        store.store1,
    ]

    dataset = {dataset.__name__: dataset for dataset in datasets}[dataset_name]

    # generate data
    dataset(limit, format, output_dir)

    return dataset
