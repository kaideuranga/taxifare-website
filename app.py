import streamlit as st
import requests
'''
# TaxiFareModel front
'''
st.title('Know your Taxifare')
st.markdown('Please enter the details')

st.header('Details')
pickup_date= st.date_input('Date', value=None, min_value=None, max_value=None)
pickup_time= st.time_input('Time',value=None)
pickup_longitude= st.text_input('Pickup longitude')
pickup_latitude= st.text_input('Pickup latitude')
dropoff_longitude= st.text_input('Dropoff longitude')
dropoff_latitude= st.text_input('Dropoff latitude')
passenger_count= st.selectbox('Number of passengers', [1,2,3,4])

url = 'https://taxifare.lewagon.ai/predict'

def get_prediction():

    params_dict = {
        'pickup_datetime': f"{pickup_date} {pickup_time}",
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    response = requests.get(url, params= params_dict)
    prediction = response.json()
    pred = prediction['fare']
    st.header(f'Fare amount: ${round(pred, 2)}')
        #else:
            #print(pickup_time)
            #st.error('Please check your input data.')
    #except requests.exceptions.RequestException as e:
            #st.error(f'Error: {e}. Failed to connect to the API.')

if st.button('Get fare prediction'):
    get_prediction()
