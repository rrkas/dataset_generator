import json
import os
import xml.etree.ElementTree as ET

import pandas as pd
import yaml


def dict_to_xml(data: list):
    root = ET.Element("data")
    for e in data:
        entry = ET.SubElement(root, "entry")
        for key, value in e.items():
            sub = ET.SubElement(entry, key)
            if isinstance(value, dict):
                sub = dict_to_xml(value)
                entry.append(sub)
            else:
                sub.text = str(value)
    return root


def save_to_dir(data: list, format: str, dir_path: str):
    os.makedirs(dir_path, exist_ok=True)

    if format == "csv":
        filepath = os.path.join(dir_path, "data.csv")

        pd.DataFrame(data).to_csv(filepath, index=0)
        print(filepath)

    elif format == "json":
        filepath = os.path.join(dir_path, "data.json")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    data,
                    indent=4,
                    default=str,
                )
            )

        print(filepath)

    elif format == "yaml":
        filepath = os.path.join(dir_path, "data.yaml")

        formatted_data = {"data": {}}
        for idx, e in enumerate(data):
            formatted_data["data"][f"entry_{idx}"] = e

        with open(filepath, "w", encoding="utf-8") as f:
            yaml.dump(
                formatted_data,
                f,
            )

        print(filepath)

    elif format == "xml":
        filepath = os.path.join(dir_path, "data.xml")

        xml_data = dict_to_xml(data)
        xml_string = ET.tostring(xml_data, encoding="unicode")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml_string)

        print(filepath)

    elif format == "all":
        save_to_dir(data, "csv", dir_path)
        save_to_dir(data, "xml", dir_path)
        save_to_dir(data, "json", dir_path)
        save_to_dir(data, "yaml", dir_path)
