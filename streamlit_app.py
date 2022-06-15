import streamlit

streamlit.title('My Mons New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega3 & blueberry Oatmal')
streamlit.text('🥗kale, Spinach & Rocket smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.multiselect("Pick some fruits:*, list(my_fruit_list))
                      
                      
streamlit.dataframe(my_fruit_list)
