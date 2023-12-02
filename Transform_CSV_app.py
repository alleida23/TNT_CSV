import streamlit as st
import pandas as pd
from datetime import datetime
from function_clean_CSV import process_csv_file

# app.py

import streamlit as st
from function_clean_CSV import process_csv_file, cleanup_temp_files

# Streamlit app title
st.title("TNT Report CSV Converter To EXCEL")

# Additional information and instructions
st.write(" ")
st.write(f"### Instructions:")
st.write("1. Upload a CSV file by clicking on 'Upload a CSV TNT Express Report'.")
st.write("2. Press the 'Convert' button to process and download the converted Excel file.")
st.write(" ")

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload a CSV TNT Express Report", type=["csv"])

# Initialize a session state variable to track if conversion has been done
if "conversion_done" not in st.session_state:
    st.session_state.conversion_done = False

# Convert button
if st.button("Convert") or st.session_state.conversion_done:
    if uploaded_file is not None:
        # Read the content of the uploaded CSV file
        processed_csv, excel_name = process_csv_file(uploaded_file)
        
        # Convert DataFrame to Excel file
        try:
            processed_csv.to_excel(excel_name, index=False)
            st.write(f" ")
            st.success("**Successful Conversion to Excel File**")
            st.write(f"Download your converted file below.")
            
            # Provide download button
            st.download_button("Download TNT Report-Excel", file_name=excel_name)

            # Set the conversion_done session state variable to True
            st.session_state.conversion_done = True

        except Exception as e:
            st.error(f"Error during Excel writing: {e}")

    else:
        st.warning("No file uploaded. Please upload a CSV TNT Report.")
else:
    st.info("Upload a CSV TNT Report to convert.")

# Clean button to remove temporary files and reset the app
if st.button("Clean"):
    cleanup_temp_files()
    st.write("Temporary files cleaned.")
    
    # Reset the 'uploaded_file' variable to remove the file from "Browse files"
    uploaded_file = None

    # Reset the app by clearing session state variables
    st.session_state.clear()


