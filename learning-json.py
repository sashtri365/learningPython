#DISCLAIMER --> These all coding note is for my personal unterstanding.

#   ==>> what is json .?
# JSON is a format that used for collecting data and also use for data exchange. this format is better for human understanding.
import json
from textwrap import indent # python core have not json to support directly so we import json library to use in pthon programming.

data = {
    "name": "sashtri",
    "age": 21
}
print(type(data)) #this is dict python data type. we can change it to json string format using json.dumps().

change_format =  json.dumps(data)
print(type(change_format))   # --> this is json string format data type.

# what is the different between json.dumps() and json.dump()

# --> we use json.dumps() to convert python data type to json string format and we use json.dump() to convert python data type to json file format.
""""  Example: json.dumps  """
students = {
    "name":"sashtri",
    "age":23,
    "studying": "python"
}      # this is python programming dict data type.

change_data = json.dumps(students) # json.dumps() change python dict,list to json format string data type.

# now using file handling we can save data to file
with open("students.json","w") as file:
    file.write(change_data) # we can do similar thing using json.dump() shortcut method
print(type(change_data))

# if wwe need to change python data type to json and save to file we can do both work at one time using json.dump
with open("students.json","w") as file:
   json.dump(students, file, indent=4)
 