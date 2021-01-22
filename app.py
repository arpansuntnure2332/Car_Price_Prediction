from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_model.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    

    if request.method == 'POST':
        Year = int(request.form['Year'])
        
        Kms_Driven=int(request.form['Kms_Driven'])
        
        Mileage=float(request.form['Mileage'])
        
        Engine=int(request.form['Engine'])
        
        Max_Power=float(request.form['Max_Power'])
        
        Seatso=int(request.form['Seats'])

        if(Seatso==2):
            Seats=2
        elif(Seatso==4):
            Seats=4
        elif(Seatso==5):
            Seats=5
        elif(Seatso==6):
            Seats=6
        elif(Seatso==7):
            Seats=7
        elif(Seatso==8):
            Seats=8
        elif(Seatso==9):
            Seats=9
        elif(Seatso==10):
            Seats=10
        else:
            Seats=14

        
        Torque_Nm=float(request.form['Torque_Nm'])
        
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
                Fuel_Type_LPG=0
        elif(Fuel_Type_Petrol=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
            Fuel_Type_LPG=0
        elif(Fuel_Type_Petrol=='LPG'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0
            
        Year=2020-Year
        
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
            Seller_Type_Trustmark_Dealer=0
        elif(Seller_Type_Individual=='Trustmark Dealer'):
            Seller_Type_Individual=0
            Seller_Type_Trustmark_Dealer=1
        else:
            Seller_Type_Individual=0
            Seller_Type_Trustmark_Dealer=0
            
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0

        prediction=model.predict([[Kms_Driven,Mileage,Engine,Max_Power,Seats,Torque_Nm,Year,Fuel_Type_Diesel,Fuel_Type_LPG,Fuel_Type_Petrol,Seller_Type_Individual,Seller_Type_Trustmark_Dealer,Transmission_Mannual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

