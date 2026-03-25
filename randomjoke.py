import streamlit as st
import requests

st.title("Random Joke Generator")
if st.button("Get Joke"):
    url="https://official-joke-api.appspot.com/random_joke"
    with st.spinner("Fetching a Funny Joke..."):
        resp=requests.get(url)
    if resp.status_code==200:
        data=resp.json()
        st.write("### Here's ur Joke: ")
        st.success(data["setup"])
        st.info(data["punchline"])
    else:
        st.error("failed to fetch a Joke. Try again!")
        
    

