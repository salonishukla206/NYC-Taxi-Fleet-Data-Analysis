#loading important libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly 
import plotly.express as px
import seaborn as sns
import pydeck as pdk
import folium
from streamlit_folium import folium_static
from PIL import Image
###################################################

st.set_page_config(page_title = 'Travelling Town', page_icon= ' :car:')

logo = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\log.PNG')

st.image(logo,width=1000,use_column_width=False)
st.markdown (' Get Started with Guide')
if st.button('Welcome Guide'):
    col1, col2, col3 = st.beta_columns(3)
    col1.markdown("Travelling Town's aims to help the small taxi services to generate maximum revenue with minimum capital. Using Travelling Town, A person with even a single car can take free advice and make a data-driven decision. Follow the instructions and explore the graphs wisely. Your profit is on the way. 😃")
    taxi = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\taxi.JPG')

    col2.image(taxi,width=500,use_column_width=False)
    
#################################################
#Loading data 
Data_url = (r"C:\Users\Sanidhya\Downloads\Minor\r.csv")
def load_data(nrows):
    df = pd.read_csv(Data_url, nrows=nrows)
    #extracting weekdays
    df['PickupTime'] = pd.to_datetime(df['PickupTime'], errors='coerce')
    df['weekday'] = df['PickupTime'].dt.dayofweek
    df['Manhattan'] = df['Manhattan']*100
    df['JFK'] = df['JFK']*100
    df['LaGuardia'] = df['LaGuardia']*100 
    df.dropna(subset =['latitude', 'longitude'], inplace=True)
    return df

df = load_data(10000)
lal =  (r"C:\Users\Sanidhya\Downloads\Minor\Locations.csv")
data = pd.read_csv(lal)   


city_select = st.selectbox(
    label = "Select the targeted city of NYC",
    options=['None','Manhattan', 'JFK', 'LaGuardia']
)

######################################################
if city_select == 'None' :
    nyc = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\nyc.JPG')
    st.image(nyc,width=1000, use_column_width = False)
        
    

elif city_select == 'Manhattan':

    
#World map pointing to Manhattan map
    q1 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\q1.PNG')
    st.image(q1,width = 800,use_column_width=False)
    f1 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\f1.PNG')
    if st.button('Happy to Help 😊') :
        st.image(f1,width=1000,use_column_width=False)
    

    map_select = st.selectbox(
        label = "Which Map would you like to see? ",
        options = ['None', 'Terrain Map', 'Street Map', 'Both the maps']
        )
    if map_select == 'None':
        p = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\welcome.JPG')
        st.image(p,width=500,use_column_width=False)
    
    elif map_select =='Terrain Map':
            st.title('Terrain View')
            df1 = pd.DataFrame(   
            np.random.randn(1000, 2) / [10, 10] + [40.754932, -73.984016],
            columns=['latitude', 'longitude'])
            st.map(df1)
        
    elif map_select == 'Street Map':
            st.title('Street View')
            m = folium.Map(location=[40.754932, -73.1084016], zoom_start=16)
            tooltip = "Manhattan"
            folium.Marker(
            [40.754932, -73.984016], popup="Manhattan", tooltip=tooltip).add_to(m)
            folium_static(m)
    else:
             st.title('Terrain View')
             df1 = pd.DataFrame(   
             np.random.randn(1000, 2) / [10, 10] + [40.754932, -73.984016],
             columns=['latitude', 'longitude'])
             st.map(df1)
             st.title('Street View')
             m = folium.Map(location=[40.754932, -73.1084016], zoom_start=16)
             tooltip = "Manhattan"
             folium.Marker(
             [40.754932, -73.984016], popup="Manhattan", tooltip=tooltip).add_to(m)
             folium_static(m)
    
    #Graphs
    chart_select = st.selectbox(
    label = "Select the chart type",
    options=['None','Scatterplots','Altair Chart']
    )
    if chart_select == 'None':
        st.text('My friend, you need more exploration to make wiser descision')
    elif chart_select == 'Scatterplots':
        st.markdown('**_Scatterplot_**')
        #m = df['Manhattan']*100
        plot = px.scatter(data_frame = df, x= df['Manhattan'], y = df['HourOfDay'] )
        st.plotly_chart(plot) 
        if st.checkbox('Get help to analyse the graph', False):
            p1 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\p1.PNG')
            st.image(p1,width = 1000,use_column_width=False)
    else:     
        st.markdown('**_Altair Chart_**')
        chart = alt.Chart(df).mark_circle().encode(
        x = 'weekday', y = 'Manhattan', tooltip = [ 'Manhattan', 'weekday']
        )
        st.altair_chart(chart)
        if st.checkbox('Get help to analyse the graph', False):
            p2 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\p2.PNG')
            st.image(p2,width = 1000,use_column_width=False)
    if st.button ('Explore More?'):
        st.markdown('Great choice !!!')
        st.markdown('Line graph is here to help you to compare your selected city with other cities of NYC 🗽')       
        chart_data = pd.DataFrame(
        np.random.randn(24, 3),
        columns=['Manhattan', 'LaGuardia', 'JFK'])
        st.line_chart(chart_data)
        
        
 ######################################################       
elif city_select == 'JFK':
#World map pointing to JFK map
    q2 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\q2.PNG')
    st.image(q2,width = 500,use_column_width=False)
    f1 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\f1.PNG')
    if st.button('Happy to Help 😊') :
        st.image(f1,width=500,use_column_width=False)
    

    map_select = st.selectbox(
        label = "Which Map would you like to see? ",
        options = ['None', 'Terrain Map', 'Street Map', 'Both the maps']
        )
    if map_select == 'None':
        w2 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\w2.JPG')
        st.image(w2,width=500,use_column_width=False)
    
    elif map_select =='Terrain Map':
            st.title('Terrain View')
            df1 = pd.DataFrame(   
            np.random.randn(1000, 2) / [10, 10] + [40.7730, -73.8702],
            columns=['latitude', 'longitude'])
            st.map(df1)
        
    elif map_select == 'Street Map':
            st.title('Street View')
            m = folium.Map(location=[40.7730, -73.8702], zoom_start=16)
            tooltip = "Manhattan"
            folium.Marker(
            [40.754932, -73.984016], popup="JFK", tooltip=tooltip).add_to(m)
            folium_static(m)
    else:
             st.title('Terrain View')
             df1 = pd.DataFrame(   
             np.random.randn(1000, 2) / [10, 10] + [40.7730, -73.8702],
             columns=['latitude', 'longitude'])
             st.map(df1)
             st.title('Street View')
             m = folium.Map(location=[40.7730, -73.8702], zoom_start=16)
             tooltip = "JFK"
             folium.Marker(
             [40.7730, -73.8702], popup="JFK", tooltip=tooltip).add_to(m)
             folium_static(m)
    
    #Graphs
    chart_select = st.selectbox(
    label = "Select the chart type",
    options=['None','Scatterplots','Altair Chart']
    )
    if chart_select == 'None':
        st.text('My friend, you need more exploration to make wiser descision')
    elif chart_select == 'Scatterplots':
        st.markdown('**_Scatterplot_**')
        plot = px.scatter(data_frame = df, x= df['JFK'], y = df['HourOfDay'] )
        st.plotly_chart(plot) 
        if st.checkbox('Get help to analyse the graph', False):
            p1 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\p1.PNG')
            st.image(p1,width = 1000,use_column_width=False)
    else:     
        st.markdown('**_Altair Chart_**')
        chart = alt.Chart(df).mark_circle().encode(
        x = 'weekday', y = 'JFK', tooltip = [ 'JFK', 'weekday']
        )
        st.altair_chart(chart)
        if st.checkbox('Get help to analyse the graph', False):
            p2 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\p2.PNG')
            st.image(p2,width = 1000,use_column_width=False)
            
    if st.button ('Explore More?'):
        st.markdown('Great choice !!!')
        st.markdown('Line graph is here to help you to compare your selected city with other cities of NYC 🗽')       
        chart_data = pd.DataFrame(
        np.random.randn(24, 3),
        columns=['Manhattan', 'LaGuardia', 'JFK'])
        st.line_chart(chart_data)
    
 #####################################################################       
else:
    q3 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\q3.PNG')
    st.image(q3,width = 500,use_column_width=False)
    f1 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\f1.PNG')
    if st.button('Happy to Help 😊') :
        st.image(f1,width=500,use_column_width=False)
    

    map_select = st.selectbox(
        label = "Which Map would you like to see? ",
        options = ['None', 'Terrain Map', 'Street Map', 'Both the maps']
        )
    if map_select == 'None':
        w3 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\w3.JPG')
        st.image(w3,width=500,use_column_width=False)
    
    elif map_select =='Terrain Map':
            st.title('Terrain View')
            df1 = pd.DataFrame(   
            np.random.randn(1000, 2) / [10, 10] + [40.7485, -73.7750],
            columns=['latitude', 'longitude'])
            st.map(df1)
        
    elif map_select == 'Street Map':
            st.title('Street View')
            m = folium.Map(location=[40.7485, -73.7750], zoom_start=16)
            tooltip = "Manhattan"
            folium.Marker(
            [40.7485, -73.7750], popup="JFK", tooltip=tooltip).add_to(m)
            folium_static(m)
    else:
             st.title('Terrain View')
             df1 = pd.DataFrame(   
             np.random.randn(1000, 2) / [10, 10] + [40.7485, -73.7750],
             columns=['latitude', 'longitude'])
             st.map(df1)
             st.title('Street View')
             m = folium.Map(location=[40.7485, -73.7750], zoom_start=16)
             tooltip = "JFK"
             folium.Marker(
             [40.7485, -73.7750], popup="JFK", tooltip=tooltip).add_to(m)
             folium_static(m)
    
    #Graphs
    chart_select = st.selectbox(
    label = "Select the chart type",
    options=['None','Scatterplots','Altair Chart']
    )
    if chart_select == 'None':
        st.text('My friend, you need more exploration to make wiser descision')
    elif chart_select == 'Scatterplots':
        st.markdown('**_Scatterplot_**')
        plot = px.scatter(data_frame = df, x= df['LaGuardia'], y = df['HourOfDay'] )
        st.plotly_chart(plot) 
        if st.checkbox('Get help to analyse the graph', False):
            p1 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\p1.PNG')
            st.image(p1,width = 1000,use_column_width=False)
    else:     
        st.markdown('**_Altair Chart_**')
        chart = alt.Chart(df).mark_circle().encode(
        x = 'weekday', y = 'LaGuardia', tooltip = [ 'LaGuardia', 'weekday']
        )
        st.altair_chart(chart)
        if st.checkbox('Get help to analyse the graph', False):
            p2 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\p2.PNG')
            st.image(p2,width = 1000,use_column_width=False)
            
    if st.button ('Explore More?'):
        st.markdown('Great choice !!!')
        st.markdown('Line graph is here to help you to compare your selected city with other cities of NYC 🗽')       
        chart_data = pd.DataFrame(
        np.random.randn(24, 3),
        columns=['Manhattan', 'LaGuardia', 'JFK'])
        st.line_chart(chart_data)
        


###############################################################################  
    


if st.button('Additional Info'):
    st.text('Go to side tab to get these additional information 📙')
    st.graphviz_chart("""
    digraph {
     Additional_Information -> About_Us
     Additional_Information -> Raw_Data
       
    }
""")

#display
if st.sidebar.checkbox("Show Raw Data", False):
    st.text('Please use the hour of the day you are looking for :')
    hour  = st.slider('Select Hour', 1,12,1 )
    data = df[df['HourOfDay'] == hour]
    st.subheader('Data at %sth hr of a day' % hour)
    
    st.write(data)
    
#####################################################################    
if st.sidebar.button('About Us'):
    
    st.title ('About Us')
    st.markdown('## A note to our mentor')
    st.markdown('_We, sincerely give our gratitude toward our project mentor Sh. Deepak Sant, Assistant Professor of ECE department. Under the umbrella of his guidance, our project has completed._ ')
    
    image3 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\Deepak.PNG')
    st.image(image3, caption = "Sh. Deepak Sant",width=200, use_column_width=False, clamp=False, channels='RGB', output_format='auto')
    
    st.markdown('### About Team Members: ')
    st.write('We are students of GB Pant Government Engineering College, New Delhi. ')
    st.write('Department of Electronics and Communication, Batch 2017-2021')
    image = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\Saloni.PNG')
    image1 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\shwetank.PNG')
    image2 = Image.open(r'C:\Users\Sanidhya\Downloads\Minor\Aakif.PNG')

    col1, col2, col3 = st.beta_columns(3)
    
    
    col1.image(image,width=150,use_column_width=False)
    col1.markdown("Saloni Shukla")
    

    col2.image(image1,width=150,use_column_width=False)
    col2.markdown("Shwetank Dwivedi")
    
    
    col3.image(image2,width=130,use_column_width=False)
    col3.markdown("Aakif Hussain Naqvi")
    






    



   

   























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



