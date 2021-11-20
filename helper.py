from sklearn.base import BaseEstimator, TransformerMixin
import pickle
import numpy as np
import pandas as pd

ssc_ix, hsc_ix, degree_ix, mba_ix,etest_ix = 0, 1, 2, 4,3
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_college_score=True): # no *args or **kargs
        self.add_college_score = add_college_score
    def fit(self, X, y=None):
        return self  # nothing else to do
    def transform(self, X):
        X=np.array(X)
        synthetic1 = X[:, ssc_ix]*X[:, hsc_ix]*X[:, degree_ix]*X[:, mba_ix]
        if self.add_college_score:
            synthetic2 = X[:,etest_ix]*X[:, mba_ix]
            return np.c_[X, synthetic1,synthetic2]
        else:
            return np.c_[X,synthetic1]

def predict_output(values):
    name=values['First_name']+' '+values['Last_name']
    gender=values['gender']
    ssc_p=float(values['ssc p'])
    ssc_boe=values['ssc boe']
    hsc_p=float(values['hsc p'])
    hsc_boe=values['hsc boe']
    hsc_spec=values['hsc spec']
    ug_p=float(values['ug p'])
    ug_dt=values['ug dt']
    pg_p=float(values['pg p'])
    pg_spec=values['pg spec']
    etest_p=float(values['etest p'])
    workex=values['work ex']
    
    test=pd.DataFrame([[gender,ssc_p,ssc_boe,hsc_p, hsc_boe,hsc_spec,ug_p,ug_dt,workex,etest_p,pg_spec,pg_p]],
                        columns=['gender', 'ssc_p', 'ssc_b', 'hsc_p', 'hsc_b', 'hsc_s', 'degree_p',
                                'degree_t', 'workex', 'etest_p', 'specialisation', 'mba_p'])

    model = pickle.load(open('classifier.pkl', 'rb'))
    prediction=model.predict(test)[0]

    return prediction,name

def predict_proba(data):
    gender=data['gender']
    ssc_p=float(data['ssc p'])
    ssc_boe=data['ssc boe']
    hsc_p=float(data['hsc p'])
    hsc_boe=data['hsc boe']
    hsc_spec=data['hsc spec']
    ug_p=float(data['ug p'])
    ug_dt=data['ug dt']
    pg_p=float(data['pg p'])
    pg_spec=data['pg spec']
    etest_p=float(data['etest p'])
    workex=data['work ex']
    
    test=pd.DataFrame([[gender,ssc_p,ssc_boe,hsc_p, hsc_boe,hsc_spec,ug_p,ug_dt,workex,etest_p,pg_spec,pg_p]],
                        columns=['gender', 'ssc_p', 'ssc_b', 'hsc_p', 'hsc_b', 'hsc_s', 'degree_p',
                                'degree_t', 'workex', 'etest_p', 'specialisation', 'mba_p'])
            
    model = pickle.load(open('classifier.pkl', 'rb'))
    return model.predict_proba(test)[0]