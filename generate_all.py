import os

for d in [
    "employee1",
    "employee2",
    "expense1",
    "inventory1",
    "inventory2",
    "store1",
]:
    print(d)
    os.system(
        f"python generate.py \
    --dataset {d} \
    --format all \
    --limit 10000 \
    --output-dir sample/{d}"
    )
    print()
    print()
