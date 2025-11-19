from fastapi import FastAPI

app=FastAPI()    
                  
"""
app=FastAPI():
Create a FastAPI application object.
It creates an instance of the FastAPI class.
This instance is your main application, and it is used to:
   Register routes (your API endpoints)
   Configure middleware
   Add dependencies
   Run the server
   Handle requests & responses
"""


@app.get("/")
def hello():
    return {'message':'Hello World'}

@app.get("/about")
def about():
    return {'message':'Hello folks my name is Vinayak , I am learning FastAPI'}

@app.get("/about/projects")
def projects():
    return{'Project1':'Quad Tree Visualizer',
           'Project2':'Budget Buddy',
           'Project3':'Knee-Osteoarthritis Classification using Image Processing',
           'Project4':'ChatBot'}