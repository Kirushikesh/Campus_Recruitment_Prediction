from flask import Flask, render_template, request,flash, jsonify
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

app = Flask(__name__)
app.secret_key = '8f42a73054b1749f8f58848be5e6502c'

model = pickle.load(open('classifier.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        name=request.form['First_name']+' '+request.form['Last_name']
        gender=request.form['gender']
        ssc_p=float(request.form['ssc p'])
        ssc_boe=request.form['ssc boe']
        hsc_p=float(request.form['hsc p'])
        hsc_boe=request.form['hsc boe']
        hsc_spec=request.form['hsc spec']
        ug_p=float(request.form['ug p'])
        ug_dt=request.form['ug dt']
        pg_p=float(request.form['pg p'])
        pg_spec=request.form['pg spec']
        etest_p=float(request.form['etest p'])
        workex=request.form['work ex']
        
        test=pd.DataFrame([[gender,ssc_p,ssc_boe,hsc_p, hsc_boe,hsc_spec,ug_p,ug_dt,workex,etest_p,pg_spec,pg_p]],
                            columns=['gender', 'ssc_p', 'ssc_b', 'hsc_p', 'hsc_b', 'hsc_s', 'degree_p',
                                    'degree_t', 'workex', 'etest_p', 'specialisation', 'mba_p'])
    
        prediction=model.predict(test)[0]
        
        if(prediction==1):
            flash(f"Congrats {name} the chances for you to get placed is high!!",'success')
            return render_template('home.html')
        else:
            flash(f"Sorry {name} Based on your data the chance of getting recruited is low",'danger')
            return render_template('home.html')
    else:
        return render_template('home.html')

@app.route("/result", methods=['POST'])
def result():
    data = request.get_json(force=True)

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

    prediction=model.predict_proba(test)[0]

    return jsonify({'Not Placed': prediction[0],'Placed': prediction[1]})

if __name__=="__main__":
    app.run()
