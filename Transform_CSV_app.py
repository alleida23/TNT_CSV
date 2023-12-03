# Import necessary libraries
import streamlit as st
import pandas as pd
from datetime import datetime
import subprocess

# Install openpyxl within the Streamlit app
subprocess.run(["pip", "install", "openpyxl"])


# Streamlit app title
st.title("TNT Report CSV Converter To EXCEL")

# Additional information and instructions
st.write(" ")
st.write(f"### Instructions:")
st.info("1. Upload a CSV file by clicking on 'Upload a CSV TNT Express Report'.")
st.info("2. Press the 'Convert' button to process and download the converted Excel file.")
st.write(" ")

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload a CSV TNT Express Report", type=["csv"])

# Initialize a session state variable to track if conversion has been done
if "conversion_done" not in st.session_state:
    st.session_state.conversion_done = False

# Convert button
if st.button("Convert") or st.session_state.conversion_done:
    if uploaded_file is not None:
        try:
            # Read the content of the uploaded CSV file
            csv = pd.read_csv(uploaded_file, sep=r',""', header=0, encoding="utf-8", engine='python')
            # 1) Remove leading and trailing whitespaces from column names and all values in all columns
            csv.columns = csv.columns.str.strip('"')
            csv = csv.apply(lambda x: x.str.strip('"'))
                
            # 2) Remove "/" from 'Shipment reference'
            csv['Shipment reference'] = csv['Shipment reference'].str.replace('/', '')
                
            # 3) Convert 'Number of Packages' to integer
            csv['Number of Packages'] = csv['Number of Packages'].astype(int)
                
            # 4) Convert 'Total weight' to float with 1 decimal
            csv['Total weight'] = csv['Total weight'].astype(float).round(1)
                
            # 5) Convert 'Total volume' to float with 3 decimals
            csv['Total volume'] = csv['Total volume'].astype(float).round(3)
                
            # 6) List of columns to capitalize
            columns_to_capitalize = ['Sender contact name', 'Sender city', 'Collection city', 'Receiver city', 'Delivery city', 'Tracking status']
                
            # Loop through specified columns and capitalize values
            for col in columns_to_capitalize:
                csv[col] = csv[col].str.title()
                
            # Generate a timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                
            # Specify the desired Excel file name
            excel_file_name = f'TNT_Track_Report_{timestamp}.xlsx'
            
            st.write(csv.head(2))
            st.write(f"{excel_file_name}")

            # Save the Excel file without using openpyxl
            csv.to_excel(excel_file_name, index=False)

            # Add a download button for the Excel file
            st.download_button(
                label="Download Excel File",
                data=None,
                file_name=excel_file_name,
                key="download_excel_button",
                help="Click here to download the Excel file."
            )

        except Exception as e:
            # Handle exceptions, e.g., invalid CSV format
            st.error(f"Error reading CSV file: {e}")
