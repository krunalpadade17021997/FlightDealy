from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import datetime
import numpy as np



app = Flask(__name__)
model = pickle.load(open("classificationModify.pkl", "rb"))
@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():

    temp_array = list()

    if request.method == "POST":
        # Arrival
        date_arr = request.form["CRSArrTime"]
        Arrival_day = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").day)
        Arrival_month = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").month)
        Arrival_year = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").year)
        
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

        # CRSArrTime
        CAT = str(Arrival_hour) + str(Arrival_min)
        CRSArrTime = int(CAT)
        #temp_array = temp_array + CRSArrTime

        # Date_of_Journey
        date_dep = request.form["CRSDepTime"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        Journey_year = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").year)
        #print("Journey Date : ",date_dep,Journey_day, Journey_month,Journey_year)

        # CRSDepTime
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        
        CDT = str(Dep_hour) + str(Dep_min)
        CRSDepTime = int(CDT)
        #temp_array = temp_array + CRSDepTime

        # dayofmonth
        DayofMonth = Arrival_day
        #temp_array = temp_array + DayofMonth

        # Destination
        Destination = request.form["Destination"]
        if (Destination == 'ATL'):
            D_ATL = 0
            Destination = D_ATL
    
        elif (Destination == 'CLT'):
            D_CLT = 1
            Destination = D_CLT
    
        elif (Destination == 'DEN'):
            D_DEN = 2
            Destination = D_DEN
    
        elif (Destination == 'DFW'):
            D_DFW = 3
            Destination = D_DFW
            
        elif (Destination == 'EWR'):
            D_EWR = 4
            Destination = D_EWR
     
        elif (Destination == 'IAH'):
            D_IAH = 5
            Destination = D_IAH   
            
        elif (Destination == 'JFK'):
            D_JFK = 6
            Destination = D_JFK
            
        elif (Destination == 'LAS'):
            D_LAS = 7
            Destination = D_LAS
            
        elif (Destination == 'LAX'):
            D_LAX = 8
            Destination = D_LAX
            
        elif (Destination == 'MCO'):
            D_MCO = 9
            Destination = D_MCO
            
        elif (Destination == 'MIA'):
            D_MIA = 10
            Destination = D_MIA
            
        elif (Destination == 'ORD'):
            D_ORD = 11
            Destination = D_ORD
            
        elif (Destination == 'PHX'):
            D_PHX = 12
            Destination = D_PHX
            
        elif (Destination == 'SEA'):
            D_SEA = 13
            Destination = D_SEA
            
        elif (Destination == 'SFO'):
            D_SFO = 14
            Destination = D_SFO
            
        #temp_array = temp_array + Destination


        # month
        Month = Arrival_month
        #temp_array = temp_array + Month


        # Origin
        Origin = request.form["Origin"]
        if (Origin == 'ATL'):
            O_ATL = 0
            Origin = O_ATL
            

        elif (Origin == 'CLT'):
            O_CLT = 1 
            Origin = O_CLT

        elif (Origin == 'DEN'):
            O_DEN = 2
            Origin = O_DEN

        elif (Origin == 'DFW'):
            O_DFW = 3
            Origin = O_DFW
            
        elif (Origin == 'EWR'):
            O_EWR = 4
            Origin = O_EWR
     
        elif (Origin == 'IAH'):
            O_IAH = 5
            Origin = O_IAH
                
        elif (Origin == 'JFK'):
            O_JFK = 6
            Origin = O_JFK
            
        elif (Origin == 'LAS'):
            O_LAS = 7
            Origin = O_LAS
            
        elif (Origin == 'LAX'):
            O_LAX = 8
            Origin = O_LAX
            
        elif (Origin == 'MCO'):
            O_MCO = 9
            Origin = O_MCO
            
        elif (Origin == 'MIA'):
            O_MIA = 10
            Origin = O_MIA 
            
        elif (Origin == 'ORD'):
            O_ORD = 11
            Origin = O_ORD
            
        elif (Origin == 'PHX'):
            O_PHX = 12
            Origin = O_PHX
            
        elif (Origin == 'SEA'):
            O_SEA = 13
            Origin = O_SEA
            
        elif (Origin == 'SFO'):
            O_SFO = 14
            Origin = O_SFO
        #else:
            # '';
            
       # print(O_ATL, O_CLT, O_DEN, O_DFW, O_EWR , O_IAH, O_JFK , O_LAS, O_LAX,  O_MCO, O_MIA, O_ORD, O_PHX, O_SEA, O_SFO);
           
        #temp_array = temp_array + Origin


        # Quater
        Q1 = [1,2,3]
        Q2 = [4,5,6]
        Q3 = [7,8,9]
        #Q4 = [10,11,12] 
        
        if Arrival_month in Q1:
            Quarter = 1
        elif Arrival_month in Q2:
            Quarter = 2
        elif Arrival_month in Q3:
            Quarter = 3
        else :
            Quarter = 4
            
        #temp_array = temp_array + Quarter

        # year
        Year = Arrival_year
        #temp_array = temp_array + Year

        # Airlines
        # {0: 'AA', 1: 'AS', 2: 'B6', 3: 'DL', 4: 'F9', 5: 'OO', 6: 'UA', 7: 'VX', 8: 'WN'}

        airline=request.form['UniqueCarrier']
        if (airline == 'AA'):
            airline = 0
        elif (airline == 'AS'):
            airline = 1
        elif (airline == 'B6'):
            airline = 2
        elif (airline == 'DL'):
            airline = 3
        elif (airline == 'F9'):
            airline = 4
        elif (airline == 'OO'):
            airline = 5
        elif (airline == 'UA'):
            airline = 6
        elif (airline == 'VX'):
            airline = 7
        elif (airline == 'WN'):
            airline = 8
        


        # weather data
        windspeedKmph = 12
        winddirDegree = 186
        precipMM = 1
        visibility = 9
        pressure = 1016
        cloudcover = 42
        DewPointF = 49
        WindGustKmph = 16
        tempF = 65
        WindChillF = 63
        humidity = 63   
                                                                                # airline
        temp_array = temp_array + [CRSArrTime,CRSDepTime,DayofMonth,Destination,Month,Origin,Quarter,Year,
                                   windspeedKmph, winddirDegree, precipMM, visibility, pressure,cloudcover,DewPointF,WindGustKmph,tempF,WindChillF,humidity]

        data = np.array([temp_array])
        my_prediction = int(model.predict(data)[0])
        
    
    # Classification
    if my_prediction == 0:
        return render_template('home.html',prediction_text=" Your Flight won't delay")
    else:
        return render_template('home.html',prediction_text=" Your Flight will delay")

if __name__ == '__main__':
	app.run(debug=True)