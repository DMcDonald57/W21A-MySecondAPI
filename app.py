from flask import Flask, request
import json
from dbhelpers import run_statement

app = Flask(__name__)

@app.get('/api/items')
def itemlist():
    result = run_statement('CALL itemlist')
    if (type(result) == list):
        return json.dumps(result, default=str)
    else:
        return "There was an error"

# This post works as it added item to DB but return message does not.  I still get error msg.
@app.post('/api/items')
def newItem():
    name = request.json.get('name')
    description = request.json.get('description')
    quantity = request.json.get('quantity')
    result = run_statement('CALL newItem (?,?,?)',[name, description, quantity])
    if result == None:
        return "Success"
    else:
        return "There was an error"

# This patch works as it updated the quantity in the DB but return message does not.  I still get error msg.
@app.patch('/api/items')
def updateItem():
    id = request.json.get('id')
    quantity = request.json.get('quantity')
    result = run_statement('CALL updateItem (?,?)',[id,quantity])
    for quantity in result:
        return "New quantity: {}".format(quantity)
    else:
        return "There was an error"

# This delete works as it deleted the item in the DB but return message does not.  I still get error msg.

@app.delete('/api/items')
def deleteItem():
    id = request.json.get('id')
    result = run_statement('CALL deleteItem (?)',[id])
    if result == None:
        return "Item deleted"
    else:
        return "There was an error"

# The employee functions

@app.get('/api/employees')
def employeeinfo():
    id = request.json.get('id')
    result = run_statement('CALL employeeinfo (?)',[id])
    if (type(result) == list):
        return json.dumps(result, default=str)
    else:
        return "There was an error"

# # This post works as it added employee to DB but return message does not.

@app.post('/api/employees')
def newEmployee():
    name = request.json.get('name')
    hourly_wage = request.json.get('hourly_wage')
    result = run_statement('CALL newEmployee (?,?)',[name, hourly_wage])
    for name in result:
        return "Welcome {}.".format(name)
    else:
        return "There was an error"

# # This patch works as it updated the hourly wage in the DB but return message does not.
@app.patch('/api/employees')
def updateEmployee():
    id = request.json.get('id')
    hourly_wage = request.json.get('hourly_wage')
    result = run_statement('CALL updateEmployee (?,?)',[id,hourly_wage])
    for hourly_wage in result:
        return "New hourly wage: {}".format(hourly_wage)
    else:
        return "There was an error"

# # This delete works as it deleted the employee in the DB but return message does not.  I still get error msg.

@app.delete('/api/employees')
def deleteEmployee():
    id = request.json.get('id')
    result = run_statement('CALL deleteEmployee (?)',[id])
    if result == None:
        return "Employee deleted"
    else:
        return "There was an error"


app.run(debug=True)