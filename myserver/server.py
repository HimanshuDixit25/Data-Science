import uvicorn
from fastapi import FastAPI
from inputs import input
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
@app.get('/')
def index():
    return {'message': 'Hello, World'}


a = open("/Users/himanshu/Documents/python notes/myfolder/myserver/nrchmodel.pickle","rb")
model=pickle.load(a)

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}


@app.post('/predict')
def predict_average(data:input):
    data = data.dict()
    registrations    =data['registrations']
    emergencycount  =data['emergencycount']
    prescount  =data['prescount']
    investgationcount =data['investgationcount']
    medicinecount =data['medicinecount']
    admissioncount =data['admissioncount']
    dischargecount  =data['dischargecount']
    prediction = model.predict([[registrations,emergencycount,prescount,investgationcount,medicinecount,admissioncount,dischargecount]])
    
    return {
        'prediction': prediction[0]
    }
    

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)