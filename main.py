from fastapi import FastAPI, HTTPException,Path,Query
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



@app.get('/sort')
def sort_patients(sort_by : str =Query(...,description= "Sort on the basisof height,weight or bmi"),order: str = Query( 'asc',description= 'sort in asc or desc order ')):
    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code = 400 , detail =f'Invalid filed select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid order,select between asc or desc')
    
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key= lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data