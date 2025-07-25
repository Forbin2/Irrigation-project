import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
#---------------------------------------------------------

st.set_page_config(page_title= 'recommendation system',
                  layout='wide')

@st.cache_data
def get_data():
    mydata=pd.read_csv('cropdata_updated.csv')
    return mydata
data= get_data()

#--------SIDE BAR PAGE--------------------------------

st.sidebar.header('User Input Features')


crop= st.sidebar.selectbox(
    options= data['crop ID'].unique(),
    label='Select a crop:'
)

soil_type= st.sidebar.selectbox(
    options= data['soil_type'].unique(),
    label= 'Select soil type:'
)

seedling_stage= st.sidebar.selectbox(
    options=data['Seedling Stage'].unique(),
    label= 'Select seedling stage:'
)



MOI=st.sidebar.slider('Moisture content (MOI)',data['MOI'].min(),data['MOI'].max(),21)

temp=st.sidebar.slider('Temperature (temp in degree Celcius)',data['temp'].min(),data['temp'].max(),28)

humidity=st.sidebar.slider('humidity (in %)',data['humidity'].min(),data['humidity'].max(),57.89)
#------------ MAIN PAGE------------------------------------------
left_column,right_column= st.columns(2)
with left_column:
    st.header('Irrigation Recommendation System')
with right_column:
    st.image('irrigation.jpg',width=250)

st.markdown(""" 
This is a tech solution app that provide irrigation recommendation on different crops including: **Wheat**, **Carrot**,**Potato** , **Tomato**, and **Chilli**
""")

st.markdown('--------------------------------------------------------------------------------')

st.info('**Info**',icon='📌')
st.markdown(""" *The system is using default input data* **please input parameters or upload a csv file to get your predictions** """)

uploaded_file= st.sidebar.file_uploader(' **Upload a csv input file** ',type=['csv'])

if uploaded_file is not None:
    input_data= pd.read_csv(uploaded_file)
else:
    def user_input_features():
        data= {'crop ID':crop,
               'soil_type':soil_type,
               'Seedling Stage':seedling_stage,
               'MOI':MOI,
              'temp':temp,
              'humidity':humidity}
        features= pd.DataFrame(data,index=[0])
        return features

    input_data= user_input_features()
st.write(input_data)

system= pickle.load(open('model.pkl','rb'))

prediction= system.predict(input_data)
prediction_proba= system.predict_proba(input_data)

labels= pd.DataFrame({'0':'NO','1':'YES'},index=[0])
column1,column2, column3= st.columns(3)

with column1:
    st.markdown(""" **Prediction** """)
    st.write(prediction)

with column2:
    st.markdown(""" **Prediction Probability** """)
    st.write(prediction_proba)

with column3:
    st.markdown(""" **Class Labels** """)
    st.write(labels)


st.info('Recommendation',icon="🚨")

for index,pred in enumerate(prediction):
    st.write(f"{index +1}:")
    if pred==0:
        st.write('**No need for irrigation**')
    else:
        st.write('**You need to irrigate**')
        st.markdown('--------')

with st.expander('ABOUT'):
    st.markdown(""" ### GUIDANCE ON USING THIS WEB APP """)
    st.write('Welcome to a web app designed to help farmers know whether they have to irrigate or not based on daily environmental conditions, including soil moisture content, temperature, and humidity regarding your crop type, soil type, and seedling stage. ')
    st.markdown('--------------')
    st.markdown(' **Getting started** ')
    
    st.write('There there are two options for adding user input parameters; you need to select the one that best suits your needs')
    st.write('  **Option 1:** On the sidebar panel you can choose different sidebar inputs according to your preference and the predicted value will displayed on the main gape')
    st.write(' **Option 2:** You can also upload a csv file that contains your input parameters and the predicted results will be displayed on the main page as well')

    
    st.write('data source:(https://www.kaggle.com/datasets/chaitanyagopidesi/smart-agriculture-dataset)')
    
    st.write('Happy exploring')