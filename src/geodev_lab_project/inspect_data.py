# import csv

# with open("health_facilities.csv", encoding="utf-8-sig") as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)
#     # print(f"Number of rows: {len(rows)}")
#     # print(f"Columns: {list(rows[0].keys())}")

# values = []
# for row in rows:
#     value = row["x"].strip()
#     if value == "":
#         continue
#     values.append(float(value))

# print(f"Maximun: {max(values)}")
# print(f"Minimum: {min(values)}")
# print(f"Count: {len(values)}")


import csv
def inspect_column(file_name, column):
    with open (file_name) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        value = row[column].strip()
        if value == "":
            continue
        values.append(value)

    return{
        "Minimun": min(values),
        "Maximum": max(values),
        "Count": len(values)
    }

Latitude_inspection = inspect_column("health_facilities.csv", "y")
longitude_inspection = inspect_column("health_facilities.csv", "x")

print(Latitude_inspection)
print(longitude_inspection)