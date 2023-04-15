import os
import argparse

from datasets import generate_data
from datasets._save import get_doc

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

dataset = generate_data(args.dataset, args.limit, args.format, output_dir)

with open(os.path.join(output_dir, "problem_statement.txt"), "w") as f:
    f.write(get_doc(dataset))
