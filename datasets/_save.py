import json
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

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


def save_to_dir(data: list, format: str, dir_path: str, file_name: str = "data"):
    os.makedirs(dir_path, exist_ok=True)

    if format == "csv":
        filepath = os.path.join(dir_path, f"{file_name}.csv")

        pd.DataFrame(data).to_csv(filepath, index=0)
        print(filepath)

    elif format == "json":
        filepath = os.path.join(dir_path, f"{file_name}.json")

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
        filepath = os.path.join(dir_path, f"{file_name}.yaml")

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
        filepath = os.path.join(dir_path, f"{file_name}.xml")

        xml_data = dict_to_xml(data)
        xml_string = ET.tostring(xml_data, encoding="utf-8")

        dom = minidom.parseString(xml_string)
        xml_string = dom.toprettyxml()

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml_string)

        print(filepath)

    elif format == "all":
        save_to_dir(data, "csv", dir_path, file_name)
        save_to_dir(data, "xml", dir_path, file_name)
        save_to_dir(data, "json", dir_path, file_name)
        save_to_dir(data, "yaml", dir_path, file_name)


def get_doc(dataset):
    doc: str = dataset.__doc__
    lines = doc.splitlines()
    res = ""
    for line in lines:
        if len(line.strip()) == 0:
            continue
        res += line[4:].rstrip() + "\n"
    return res
