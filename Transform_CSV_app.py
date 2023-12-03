import streamlit as st
import pandas as pd
from datetime import datetime

# Streamlit app title
st.title("TNT Express Report CSV Transformer")

# Additional information and instructions
st.write(" ")
st.write(f"### Instructions:")
st.info("1. Upload a CSV file by clicking on 'Upload a CSV TNT Express Report'.")
st.info("2. Press the 'Transform' button to process and download the formatted CSV file.")
st.write(" ")

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload a CSV TNT Express Report", type=["csv"])

# Initialize a session state variable to track if transformation has been done
if "transformation_done" not in st.session_state:
    st.session_state.transformation_done = False

# Transform button
if st.button("Transform") or st.session_state.transformation_done:
    if uploaded_file is not None:
        try:
            # 0) Read the content of the uploaded CSV file
            csv = pd.read_csv(uploaded_file, sep=r',""', header=0, encoding="utf-8", engine='python', quotechar='"')

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

            # 7) Title-case the column names
            csv.columns = csv.columns.str.title()

            st.write(csv['Return Shipment Number'].unique)

            # 8) Check for empty columns and delete them
            empty_columns = [col for col in csv.columns if csv[col].empty]
            if empty_columns:
                csv = csv.drop(columns=empty_columns)
                st.write(f"Empty columns eliminated: {', '.join(empty_columns)}")

            # 9) Preview first 5 rows
            st.write("Preview:")
            st.write(csv.head(5))

            # 10) Print the shape of the DataFrame
            st.write(f"Shape: {csv.shape}")

            # 11) Display count for each unique category in 'Tracking status'
            tracking_status_count = csv['Tracking Status'].value_counts()
            st.write("Tracking Status Count:")
            st.write(tracking_status_count)

            # 12) Generate a timestamp to add to the title
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Specify the desired CSV file name
            csv_file_name = f'TNT_Track_Report_{timestamp}.csv'

            # Add a download button for the CSV file
            csv_data = csv.to_csv(index=False).encode()
            st.download_button(
                label="Download CSV File",
                data=csv_data,
                file_name=csv_file_name,
                key="download_csv_button",
                help="Click here to download the CSV file."
            )

            # Set the transformation flag to True
            st.session_state.transformation_done = True

        except Exception as e:
            # Handle exceptions, e.g., invalid CSV format
            st.error(f"Error reading CSV file: {e}")

# Clean button
if st.button("Clean"):
    # Clear uploaded file
    uploaded_file = None

    # Clear processed data
    csv = pd.DataFrame()

    # Clear session state variables
    st.session_state.transformation_done = False

    # Clear all displayed content
    st.empty()

    st.success("All data and traces have been cleared.")
