import numpy as np
import utils
from flask import Flask,render_template,request,jsonify
import traceback
from utils import config


app = Flask(__name__)

@app.route('/')
def home():
    print("This is home page")
    #return jsonify({"Health check":"Running ok"})
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        if request.method == "GET":

            data = request.args.get
            print("Data:::",data)

            age = data(('age'))
            sex = data(('sex'))
            cp = data(('cp'))
            trestbps = data(('trestbps'))
            chol = data(('chol'))
            fbs = data(('fbs'))
            restecg = data(('restecg'))
            thalach = data(('thalach'))
            exang = data(('exang'))
            oldpeak = eval(data(('oldpeak')))
            slope = data(('slope'))
            ca = data(('ca'))
            thal = data(('thal'))

            
            
            model = utils.ModelClass()

            result = model.prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
            
            output = ""
            if result == 1:
                print("Person is suffering from hypertension".upper())
                #return jsonify({"Result":"Person is suffering from hypertension".upper()})

                output = "Person is suffering from hypertension".upper()
                return render_template('index.html',prediction=output)
            else:
                print("Person is not suffering from hypertension".upper())
                #return jsonify({"Result":"Person is not suffering from hypertension".upper()})
                output = "Person is not suffering from hypertension".upper()
                return render_template('index.html',prediction=output)
        
        else:

            data = request.form.get
            print("Data:::",data)

            age = data(('age'))
            sex = data(('sex'))
            cp = data(('cp'))
            trestbps = data(('trestbps'))
            chol = data(('chol'))
            fbs = data(('fbs'))
            restecg = data(('restecg'))
            thalach = data(('thalach'))
            exang = data(('exang'))
            oldpeak = eval(data(('oldpeak')))
            slope = data(('slope'))
            ca = data(('ca'))
            thal = data(('thal'))

            
            
            model = utils.ModelClass()

            result = model.prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
            output = ""
            if result == 1:
                print("Person is suffering from hypertension".upper())
                #return jsonify({"Result":"Person is suffering from hypertension".upper()})
            
                output = "Person is suffering from hypertension".upper()
                return render_template('index.html',prediction=output)

            else:
                print("Person is not suffering from hypertension".upper())
                #return jsonify({"Result":"Person is not suffering from hypertension".upper()})
            
                output = "Person is not suffering from hypertension".upper()
                return render_template('index.html',prediction=output)
            
    except:
        print("Error occured!!")
        print("Error:",traceback.print_exc())
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=config.PORT,debug=True)
