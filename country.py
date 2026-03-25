import streamlit as st
import requests

st.title("Country Info App")

country = st.text_input("Enter Country Name:")

if st.button("Get Info"):
    if country:
        url = f"https://restcountries.com/v3.1/name/{country}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for c in data:
                st.write("### Country Details")
                st.write("Name:", c["name"]["common"])
                st.write("Capital:", c.get("capital", ["N/A"])[0])
                st.write("Population:", c["population"])
                st.image(c["flags"]["png"])
                st.write("---")
        else:
            st.error("Country not found!")
    else:
        st.warning("Please enter a country name.")
