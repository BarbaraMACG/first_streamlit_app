import streamlit
streamlit.title('My Parent New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach, Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text( '🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('fruit')
streamlit.dataframe(my_fruit_list)

# let's put a picklist here so that the user can pick the fruit the want to include 
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
