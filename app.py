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
    if result == None:
        return "Quantity updated"
    else:
        return "There was an error"

@app.delete('/api/items')
def deleteItem():
    id = request.json.get('id')
    result = run_statement('CALL deleteItem (?)',[id])
    if result == None:
        return "Item deleted"
    else:
        return "There was an error"






app.run(debug=True)