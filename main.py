from fastapi import FastAPI, Request
from mockData import products

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello world form FastAPI VENV"}

@app.get("/products")
def products_data():
    return products

# body prams
@app.get("/product/{product_id}")
def product_by_id(product_id:int):
    for productOne in products:
        if productOne.get("id") == product_id:
            return productOne
    return{
        "error":"Product not found"
    }

#query params
@app.get("/greet")
def greet(name:str, age:str):
    return{
        "data":f"Hello {name}, Your age is {age}"
    }

@app.get("/greet-request")
def greetRequest(request:Request):
    query_params = dict(request.query_params)
    return{
        "data":f"Hello {query_params.get("name")}, Your age is {query_params.get("age")}"
    }
