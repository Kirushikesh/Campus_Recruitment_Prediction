from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('logistic_regression.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        gender=request.form['Gender']
        ssc_p=request.form['SSC Percentage']
        hsc_p=request.form['HSC Percentage']
        degree_p=request.form['Degree Percentage']
        workex=request.form['Work Experience']
        etest_p=request.form['Employability test percentage']
        specialisation=request.form['Specialisation']
        mba_p=request.form['MBA Percentage']
        
        prediction=model.predict([[int(gender),float(ssc_p),float(hsc_p),float(degree_p),int(workex),float(etest_p),int(specialisation),float(mba_p)]])
        
        output=prediction[0]
        if(output==1):
            return render_template('home.html',prediction_text="Congrats the chances for you to get placed is high!!")
        else:
            return render_template('home.html',prediction_text="Based on your data the chance of getting recruited is low")
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)
