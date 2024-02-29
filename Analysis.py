import pandas
import json

filename = "tests.json"
with open(filename, "r", encoding="utf-8") as fp:
    d_table = json.load(fp)
table = pandas.DataFrame(d_table)

table.drop_duplicates(subset = ["name"], inplace = True)
for i in range(len(table)):
    table.loc[i, "name"] = table.loc[i, "name"].strip()
    table.loc[i, "number"] = table.loc[i, "number"].lstrip('/problem')
print(table)