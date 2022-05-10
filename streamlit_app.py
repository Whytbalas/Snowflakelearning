import streamlit
import pandas
streamlit.title("My Parents New Healthy diner")
streamlit.header("Breakfast Favourties")
streamlit.text("🥣Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗Kale, Spinach and Rocket Smoothie")
streamlit.text(" 🐔Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avacoda Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
myfruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
myfruit_list = myfruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(myfruit_list.index,['Avacado', 'Strawberries']))
streamlit.dataframe(myfruit_list)
