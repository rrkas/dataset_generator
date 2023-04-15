import argparse

from tqdm import tqdm

from datasets import select_dataset
from datasets._faker import MyFaker
from datasets._save import save_to_dir

parser = argparse.ArgumentParser()

parser.add_argument(
    "--dataset",
    type=str,
    help="Dataset name",
    required=True,
)
parser.add_argument(
    "--limit",
    type=int,
    default=2,
    help="Limit number of samples",
)
parser.add_argument(
    "--output-dir",
    type=str,
    help="Output directory for the data & problem statements",
    dest="output_dir",
    default=None,
)
parser.add_argument(
    "--format",
    type=str,
    default="csv",
    help="Data format",
    choices=(
        "all",
        "csv",
        "json",
        "yaml",
        "xml",
    ),
)

args = parser.parse_args()

output_dir = args.output_dir
if output_dir is None:
    output_dir = f"outputs/{args.dataset}/"

fake = MyFaker()

dataset = select_dataset(args.dataset)

data = []
for i in tqdm(range(args.limit)):
    data.append(dataset(fake))

save_to_dir(data, args.format, output_dir)
