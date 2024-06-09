from flask import Flask, request, jsonify, render_template
import sklearn
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



client = MongoClient('mongodb://localhost:27017/')
db = client['AIRBNB']
collection1 = db['AIRBNB2019']
collection2 = db['AIRBNB2023']
app = Flask(__name__)


@app.route('/Data1', methods=['GET'])
def display_graph1():
    
    data1 = collection1.find({})  
    df1 = pd.DataFrame(data1)
     
    room_counts2019 = df1['room_type'].value_counts().to_dict()
    return jsonify(room_counts2019)

@app.route('/Data2', methods=['GET'])
def display_graph2():
    
    data2 = collection2.find({})
    df2 = pd.DataFrame(data2)  
     
    room_counts2023 = df2['room_type'].value_counts().to_dict()
    return jsonify(room_counts2023)

@app.route('/Data3', methods=['GET'])
def display_graph3():
    
    data1 = collection1.find({}) 
    df1 = pd.DataFrame(data1)
     
    neighbourhood_counts2019 = df1['neighbourhood_group'].value_counts().to_dict()
    return jsonify(neighbourhood_counts2019)

@app.route('/Data4', methods=['GET'])
def display_graph4():
    
    data2 = collection2.find({})
    df2 = pd.DataFrame(data2)  
     
    neighbourhood_counts2023 = df2['neighbourhood_group'].value_counts().to_dict()
    return jsonify(neighbourhood_counts2023)      
       
@app.route('/Data5', methods=['GET'])
def display_graph5():
    
    data1 = collection1.find({})
    df1 = pd.DataFrame(data1)  
     
    neighbourhood2019 = df1['neighbourhood'].value_counts().head(10).to_dict()
    return jsonify(neighbourhood2019) 

@app.route('/Data6', methods=['GET'])
def display_graph6():
    
    data2 = collection2.find({})
    df2 = pd.DataFrame(data2)  
     
    neighbourhood2023 = df2['neighbourhood'].value_counts().head(10).to_dict()
    return jsonify(neighbourhood2023) 

@app.route('/Data7', methods=['GET'])
def display_graph7():
    
    data1 = collection1.find({})
    df1 = pd.DataFrame(data1)  
     
    neighbourhood2019 = df1['neighbourhood'].value_counts().tail(10).to_dict()
    return jsonify(neighbourhood2019) 

@app.route('/Data8', methods=['GET'])
def display_graph8():
    

    data2 = collection2.find({})
    df2 = pd.DataFrame(data2)  
     
    neighbourhood2023 = df2['neighbourhood'].value_counts().tail(10).to_dict()
    return jsonify(neighbourhood2023) 


    
@app.route('/Data9', methods=['GET'])
def get_word_cloud_data():
    data1 = collection1.find({})
    df1 = pd.DataFrame(data1)
    neighbourhood19_loc_unique = df1['neighbourhood'].unique()
    
    neighbourhood_dict = {neighbourhood: 1 for neighbourhood in neighbourhood19_loc_unique}
    
    return jsonify(neighbourhood_dict)
   
@app.route('/Data10', methods=['GET'])
def get_mean_price_data():
    data1 = collection1.find({})
    df1 = pd.DataFrame(data1)
    df1 = df1[df1.neighbourhood_group == "Brooklyn"][["neighbourhood", "price"]]
    d = df1.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))

@app.route('/Data11', methods=['GET'])
def get_mean_price():
    data1 = collection1.find({})
    df1 = pd.DataFrame(data1)
    df1 = df1[df1.neighbourhood_group == "Manhattan"][["neighbourhood", "price"]]
    d = df1.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))

@app.route('/Data12', methods=['GET'])
def get_mean_Queen():
    data1 = collection1.find({})
    df1 = pd.DataFrame(data1)
    df1 = df1[df1.neighbourhood_group == "Queens"][["neighbourhood", "price"]]
    d = df1.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))

@app.route('/Data13', methods=['GET'])
def get_mean_Bronx():
    data1 = collection1.find({})
    df1 = pd.DataFrame(data1)
    df1 = df1[df1.neighbourhood_group == "Bronx"][["neighbourhood", "price"]]
    d = df1.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))

@app.route('/Data14', methods=['GET'])
def get_mean_Staten():
    data1 = collection1.find({})
    df1 = pd.DataFrame(data1)
    df1 = df1[df1.neighbourhood_group == "Staten Island"][["neighbourhood", "price"]]
    d = df1.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))

@app.route('/Data15', methods=['GET'])
def get_mean_price_data1():
    data2 = collection2.find({})
    df2 = pd.DataFrame(data2)
    df2 = df2[df2.neighbourhood_group == "Brooklyn"][["neighbourhood", "price"]]
    d = df2.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))

@app.route('/Data16', methods=['GET'])
def get_mean_price1():
    data2 = collection2.find({})
    df2 = pd.DataFrame(data2)
    df2 = df2[df2.neighbourhood_group == "Manhattan"][["neighbourhood", "price"]]
    d = df2.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))

@app.route('/Data17', methods=['GET'])
def get_mean_Queen1():
    data2 = collection2.find({})
    df2 = pd.DataFrame(data2)
    df2 = df2[df2.neighbourhood_group == "Queens"][["neighbourhood", "price"]]
    d = df2.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))

@app.route('/Data18', methods=['GET'])
def get_mean_Bronx1():
    data2 = collection2.find({})
    df2 = pd.DataFrame(data2)
    df2 = df2[df2.neighbourhood_group == "Bronx"][["neighbourhood", "price"]]
    d = df2.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))

@app.route('/Data19', methods=['GET'])
def get_mean_Staten1():
    data2 = collection2.find({})
    df2 = pd.DataFrame(data2)
    df2 = df2[df2.neighbourhood_group == "Staten Island"][["neighbourhood", "price"]]
    d = df2.groupby("neighbourhood").mean()
    return jsonify(d.to_dict(orient='split'))





@app.route("/")
def third():
    return render_template("task.html")

@app.route("/first")
def second():
    return render_template("app.html")

@app.route("/second")
def fourth():
    return render_template("price_graphs19.html")


@app.route("/third")
def word_cloud():
    return render_template("wordcloud.html")




                                                
if __name__ == "__main__":
    app.run(debug=True)