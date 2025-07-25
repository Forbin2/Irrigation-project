# Irrigation-project
project overview:
This is a project of creating irrigation recommendation system using Logistic Regression model.
the model is trained on a dataset comprises 16,411 records related to crops, highlighting key environmental factors and their impact on growth stages. It contains details like soil type, seedling stage, moisture index (MOI), temperature, and humidity. Each entry corresponds to a specific crop sample with associated environmental conditions and an outcome.

 Features:
crop ID: Unique identifier for the crop (categorical).
soil_type: Type of soil for the crop (e.g., Black Soil, Red Soil).
Seedling Stage: The growth stage of the crop (e.g., Germination).
MOI (Moisture Index): The soil moisture content at the time of data collection (integer).
temp (Temperature): The ambient temperature in degrees Celsius (integer).
humidity: The relative humidity in percentage (float).
result: Indicates whether the crop requires irrigation or not (binary: 1 = yes, 0 = no).

 challenge addressed:
Smart farming applications can be integrated into IoT systems to automate irrigation decisions based on real-time data.

 Getting started:
There there are two options for adding user input parameters; you need to select the one that best suits your needs

Option 1: On the sidebar panel you can choose different sidebar inputs according to your preference and the predicted value will displayed on the main gape

Option 2: You can also upload a csv file that contains your input parameters and the predicted results will be displayed on the main page as well

data source: (https://www.kaggle.com/datasets/chaitanyagopidesi/smart-agriculture-dataset)
