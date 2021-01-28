
from fastapi import FastAPI
# FastAPI налогае ограничение на структуру проекта поэтому первый файл *txt а не .py!
# https://stackoverflow.com/questions/62965442/fastapi-says-missing-folder-name-as-module
from pydantic import BaseModel, validator, Field
import pickle
import pandas as pd
from itertools import combinations

app = FastAPI()

class DataRequest(BaseModel):
    features1: float = Field (..., gt=0, le=15, description=' must [0,15]')
    features2: float = Field (..., gt=0, le=15, description=' must [0,15]')
    features3: float = Field (..., gt=0, le=15, description=' must [0,15]')
    features4: float = Field (..., gt=0, le=15, description=' must [0,15]')
    features5: float = Field (..., gt=0, le=15, description=' must [0,15]')

class DataResponse(BaseModel):
    predict : float


@app.get("/")
def home():
    return {"200": "Welcome To Heroku"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# @app.post('/predict', response_model=DataResponse)
# def get_predict(data: DataRequest):
#     with open('model.pkl', 'rb') as f:
#         clf = pickle.load(f)

#     data = pd.DataFrame.from_dict([data.dict()])
#     features = data.columns.values

#     data_square = data[features].applymap(lambda x: (x * x))
#     data_square.columns = [x + '*2' for x in data[features].columns.tolist()]

#     data_prod = pd.DataFrame()
#     for n in range(2, 3):
#         for col in combinations(data_square.columns, n):
#             new_col = 'features ' + '_'.join([x[-3:] for x in col])
#             data_prod[new_col] = data_square[list(col)].prod(axis=1)

#     data = pd.concat([data_prod, data_square, data[features]], axis=1)
#     print(data.shape)
#     print(data.values)

#     y_score = clf.predict_proba(data.values)[:, 1]
#     #y_score = 0.67 pass

#     return {'predict' : y_score}
