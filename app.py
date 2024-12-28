import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_excel('EAMCET dataset.xlsx', sheet_name='data')
    return df

df = load_data()

# Streamlit App
st.title('EAMCET College Predictor')
# Set the page configuration
st.set_page_config(page_title='EAMCET College Predictor')

# User Inputs
name = st.text_input('Name *')
rank = st.number_input('EAMCET Rank *', min_value=1, step=1)
gender = st.selectbox('Gender *', ['Male', 'Female'])
caste = st.selectbox('Caste *', ['OC', 'BC_A', 'BC_B', 'BC_C', 'BC_D', 'BC_E', 'SC', 'ST', 'EWS'])
branch = st.selectbox('Branch *', df['Branch Name'].unique())

# Filter Data Button
if st.button('Show Data'):
    filtered_df = df[df['Branch Name'] == branch]
    
    if caste == 'OC':
        col = 'OC \nBOYS' if gender == 'Male' else 'OC \nGIRLS'
    else:
        col = f'{caste} \nBOYS' if gender == 'Male' else f'{caste} \nGIRLS'
    
    eligible_colleges = filtered_df[filtered_df[col] >= rank]
    
    if eligible_colleges.empty:
        st.write('No eligible colleges found for the given criteria.')
    else:
        st.write('Eligible Colleges:')
        st.dataframe(eligible_colleges[['Institute Name', 'Place', 'Branch Name', col, 'Tuition Fee']])
