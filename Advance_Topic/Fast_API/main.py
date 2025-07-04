from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# line no. 8-13 defining data structure
# pydantic 9-12
class Tea(BaseModel):
    id:int
    name:str
    origin:str

teas: List[Tea] = []    

@app.get("/")
def read():
    return {"welcome to my site"}


# performing crud opertion
# Read data
@app.get("/teas")
def get_teas():
    return teas
# add data
@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea    

# update data
@app.put("/teas/{tea_id}")
def update_tea(tea_id: int,updated_tea:Tea):
    for i,tea in enumerate(teas):
        if tea.id == tea_id:
            tea[i] = updated_tea
            return updated_tea
    return {"error":"tea not found"}        

# delete data
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for i,tea in enumerate(teas):
        if tea.id == tea_id:
          deleted = teas.pop(i)
          return deleted    
    return {"error":"tea not found"}          