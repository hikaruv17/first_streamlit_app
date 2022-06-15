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
my_fruit_list = my_fruit_list.set_index('Fruit')


fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]                       
                      
streamlit.dataframe(fruit_to_show)
