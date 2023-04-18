Fake Data Generator

$ python generate.py \
    --dataset <dataset name> \
    --format <format> \
    --limit <record count> \
    --output-dir <output dir>

arg             required        description
=====================================================================
dataset         YES             Dataset name
format          NO              Output data format, default: "csv"
limit           NO              Number of records to generate, default: 100
output-dir      NO              Output directory for the data & problem statements, default: outputs/<dataset name>/

for dataset names and schema, see datasets.txt file.
available formats:
    - csv
    - json
    - yaml
    - xml
    - xlsx
    - all
