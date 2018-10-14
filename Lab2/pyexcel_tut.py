import pyexcel 
from collections import OrderedDict

data = [
    OrderedDict({
        "Name": "Hanh",
        "Age": 23,
        'City': 'Hai Duong'
    }),
    OrderedDict({
        "Name": "Hoang",
        "Age": 24,
        "City": 'Ha Noi'
    }),
    OrderedDict({
        "Name": "Hogi",
        "Age": 20,
        "City": 'TP HCM'
    }),
]

pyexcel.save_as(records=data, dest_file_name='sample.xlsx')