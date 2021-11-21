from flask import Flask, render_template, request,flash, jsonify
from helper import predict_output,predict_proba,CombinedAttributesAdder

import __main__
__main__.CombinedAttributesAdder= CombinedAttributesAdder

app = Flask(__name__)
app.secret_key = '8f42a73054b1749f8f58848be5e6502c'

@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        
        prediction,name=predict_output(request.form)
        
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
    prediction=predict_proba(data)
    return jsonify({'Not Placed': prediction[0],'Placed': prediction[1]})

if __name__=="__main__":
    app.run()
