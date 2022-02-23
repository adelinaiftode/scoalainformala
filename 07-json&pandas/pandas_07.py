import pandas as pd
import ssl

# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renault'],
#     "culoare": ['rosu', 'alb', 'verde']
# }
#
# variabila = pd.DataFrame(dictionar_date)
# print(variabila)

# masini = ['Dacia', 'Volvo', 'Renault']
# variabila = pd.Series(masini, index=["x", "y", "z"])
# print(variabila["z"])
# print(variabila[0])

# masini = {"x": "Dacia", "y": "Volvo", "z": "Renault"}
# variabila = pd.Series(masini, index=["y", "z"])
# print(variabila)


dictionar_date = {
    "masini": ['Dacia', 'Volvo', 'Renault'],
    "culoare": ['rosu', 'alb', 'verde']
}

variabila = pd.DataFrame(dictionar_date, index=["producator1", "producator2", "producator3"])
# print(variabila.loc[[0, 1]])
print(variabila.loc[["producator1", "producator2"]])



data = {
  "producator1": {
    "masini": "Dacia",
    "culoare": "rosu"
  },
  "producator2": {
    "masini": "Volvo",
    "culoare": "alb"
  },
  "producator3": {
    "masini": "Renault",
    "culoare": "verde"
  }
}

variabila1 = pd.DataFrame(data)
# variabila1 = pd.read_json('data.json')
# url = 'https://api.exchangerate-api.com/v4/latest/USD'
# variabila2 = pd.read_json(url)
# print(variabila2)

fisier = variabila1.to_csv("data.csv")
