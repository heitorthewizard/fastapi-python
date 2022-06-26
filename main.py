# Creating an API with FastAPI
# Fast, Documentation and Asynchronism
# uvicorn is been used to run a local server

# calling fast api
import string
from fastapi import FastAPI

# creating an instance of FastAPI as 'app'
app = FastAPI()

# after calling fast api, you can run uvicorn, run it:
# uvicorn main:app --reload 
# ((file-name):(named-instance))
# --reload => allows us to change api on server when changes are made here.

# simulating sales
sales = {
    1: {
        'item': 'laptop',
        'price': 1500,
        'amount': 1
    },
    2: {
        'item': 'mouse',
        'price': 45,
        'amount': 1
    },
    3: {
        'item': 'mouse pad',
        'price': 10,
        'amount': 1
    },
    4: {
        'item': 'monitor',
        'price': 500,
        'amount': 2
    },
    5: {
        'item': 'gamer chair',
        'price': 800,
        'amount': 1
    },
    6: {
        'item': 'coffee bag',
        'price': 10,
        'amount': 50
    }
}


# '@' decorator = a statement made in a line of code that will
# give functionalities to the line of code below it
@app.get('/')  # route to access via link

# after that is done, you can enter "/docs" and check the documentation
# we returning in a RestAPI way (json format)
def home():
    return {
        'total sales': len(sales)
    }  # return the total sales

# creating a route for accessing details from sales
@app.get('/sales/{id_sale}')  # decorator, again
def get_sales(id_sale: int):  # types are optional (str, int, etc) 
    return sales[id_sale]     # but really recommended to use 

@app.get('/secret')
def secret_message():
    return {
        'message': 'THIS IS MY FIRST API!!'
    }
    