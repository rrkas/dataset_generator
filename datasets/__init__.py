from . import employee


def select_dataset(dataset_name: str):
    datasets = [
        employee.employee1,
    ]

    return {dataset.__name__: dataset for dataset in datasets}[dataset_name]
    # return {dataset.__name__: dataset for dataset in datasets}
