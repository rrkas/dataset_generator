import os
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
    default=100,
    help="Number of records to generate",
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
    help="Output data format",
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

with open(os.path.join(output_dir, "problem_statement.txt"), "w") as f:
    f.write(dataset.__doc__.strip())
