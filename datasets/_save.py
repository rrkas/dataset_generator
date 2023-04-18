import json
import os
import xml.dom.minidom as minidom
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


def save_to_dir(data: dict, format: str, dir_path: str):
    os.makedirs(dir_path, exist_ok=True)

    if format in ["xlsx", "all"]:
        filepath = os.path.join(dir_path, f"data.xlsx")
        print(filepath)
        with pd.ExcelWriter(filepath) as writer:
            for sheet, d in data.items():
                pd.DataFrame(d).to_excel(writer, sheet, index=0)

    if format in ["csv", "all"]:
        for sheet, d in data.items():
            filepath = os.path.join(dir_path, f"{sheet}.csv")

            pd.DataFrame(d).to_csv(filepath, index=0)
            print(filepath)

    if format in ["json", "all"]:
        for sheet, d in data.items():
            filepath = os.path.join(dir_path, f"{sheet}.json")

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        d,
                        indent=4,
                        default=str,
                    )
                )

            print(filepath)

    if format in ["yaml", "all"]:
        for sheet, d in data.items():
            filepath = os.path.join(dir_path, f"{sheet}.yaml")

            formatted_data = {"data": {}}
            for idx, e in enumerate(d):
                formatted_data["data"][f"entry_{idx}"] = e

            with open(filepath, "w", encoding="utf-8") as f:
                yaml.dump(
                    formatted_data,
                    f,
                )

            print(filepath)

    if format in ["xml", "all"]:
        for sheet, d in data.items():
            filepath = os.path.join(dir_path, f"{sheet}.xml")

            xml_data = dict_to_xml(d)
            xml_string = ET.tostring(xml_data, encoding="utf-8")

            dom = minidom.parseString(xml_string)
            xml_string = dom.toprettyxml()

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(xml_string)

            print(filepath)


def get_doc(dataset):
    doc: str = dataset.__doc__
    lines = doc.splitlines()
    res = ""
    for line in lines:
        if len(line.strip()) == 0:
            continue
        res += line[4:].rstrip() + "\n"
    return res
