from fastapi import FastAPI, HTTPException,Path
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data

#create routes or endpoints
@app.get("/")
def hello():
    return {'message' : 'Patient Management Systems API'}


@app.get('/about')
def about():
    return{'message' : 'A Fully Functioning API to manage your patients records'}


@app.get('/view')
def view():
    data =load_data()

    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id:str = Path(...,description= 'ID of the patient in the Db' , example= 'P001' )):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    #return {'error' : 'Patient not found'}
    raise HTTPException(status_code=404, detail="Patient not found")

# path function in FastApi is used to provide Metadata,validation rules, and documentation hints for path parameter 
# in your API endpoints


