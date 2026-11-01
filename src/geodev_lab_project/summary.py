import csv
def read_rows(file_name):
    with open (file_name, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = [float(row[column]) for row in rows]
    return values

def summarise(values):
    if len(values) == 0:
        return {
            "smallest": None,
            "largest": None,
            "count": 0,
            "average": None,
        }
    return{
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
        "average": sum(values) / len(values),
    }


def summarise_all(file_name, columns):
    rows = read_rows(file_name)
    reports={}
    for column in columns:
        values = clean_values(rows, column)
        reports[column] = summarise(values)
    return reports

report = summarise_all("health_facilities.csv", ["x", "y"])
for column, stat in report.items():
    print( column, "->", stat)
