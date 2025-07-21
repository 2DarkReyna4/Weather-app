import streamlit as st
import requests
import json


key='3dc805f06f7a44beae1132124250807'
st.title('weather app ☁️')
st.subheader('This application help in finding the weather of a particular city')
city=st.text_input('enter a city name')
if st.button('display'):
    p = {
        'appid': key,
        'q': city
    }
    base_url = f"http://api.weatherapi.com/v1/current.json?key=3dc805f06f7a44beae1132124250807&q={city}&aqi=no"
    result = requests.get(base_url, params=p)
    if result.status_code==200:
        result = requests.get(base_url, params=p).json()



        icon_=result['current']['condition']['icon']
        icon_='https:'+icon_
        st.image(icon_,width=100)
        st.subheader(f"Weather information of {city} ☁️")
        st.subheader(f"date and time: {result['location']['localtime']} 🕰️")
        st.write(f"The temperature is {result['current']['temp_c']} C")
        st.write(f"The wind speed is {result['current']['wind_kph']} km/h")
        st.write(f"The UV index is {result['current']['uv']}")
        st.write(f"It is {result['current']['condition']['text']}")
        st.write(f"The humidity is {result['current']['humidity']}")
    else:
        st.error("please enter a valid city name")
