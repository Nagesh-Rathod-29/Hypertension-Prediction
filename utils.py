import pickle
import json
import numpy as np
import keras
import traceback
import config

class ModelClass:

    def __init__(self):

        self.model = keras.models.load_model(config.MODEL_FILE_PATH)

        self.scaler = pickle.load(open(config.SCALER_FILE_PATH,'rb'))

        self.model_features = json.load(open(config.MODEL_FEATURES_FILE,'r'))

    
    def prediction(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):

        input_array = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])

        reshaped_array = input_array.reshape(1,-1)

        scaled_array = self.scaler.transform(reshaped_array)

        prob = self.model.predict(scaled_array)

        pred = np.where(prob>0.5,1,0)

        #if pred[0] == 1:
        #    print("person is suffering from hypertension".upper())

        #else:
        #    print("person is not suffering from hypertension".upper())
        
        return pred[0]
    

#if __name__ == "__main__":
#    test = ModelClass()
#    test.prediction(48.0, 1.0, 0.0, 120.0, 229.0, 0.0, 0.0, 129.0, 1.0, 2.6, 1.0, 2.0, 3.0)