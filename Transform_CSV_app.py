# Transform_CSV_app.py

# Import necessary libraries
import streamlit as st
from function_clean_CSV import process_csv_file, cleanup_temp_files
import pandas as pd

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
            content = uploaded_file.read().decode('utf-8')
            # Separator (',""')
            separator = ',""'
            # Use pandas to read the CSV content with the specified separator
            processed_csv = pd.read_csv(pd.compat.StringIO(content), sep=separator, header=0, encoding="utf-8", engine='python')

            display(processed_csv.head(2))

            # ... (the rest of your conversion logic)

        except Exception as e:
            # Handle exceptions, e.g., invalid CSV format
            st.error(f"Error reading CSV file: {e}")
        
        
     #   processed_csv, excel_name = process_csv_file(uploaded_file)
        
        # Convert DataFrame to Excel file
      #  try:
            # Writing the processed CSV to an Excel file
       #     processed_csv.to_excel(excel_name, index=False)
            
            # Display success message and provide download button
        #    st.write(f" ")
        #    st.success("**Successful Conversion to Excel File**")
        #    st.write(f"Download your converted file below.")
        #    st.download_button("Download TNT Report-Excel", file_name=excel_name)

            # Clean up temporary files and uploaded file
         #   cleanup_temp_files(excel_name, uploaded_file.name)

            # Set the conversion_done session state variable to True
          #  st.session_state.conversion_done = True

#        except Exception as e:
            # Display error message in case of an exception
 #           st.error(f"Error during Excel writing: {e}")
  #  else:
        # Display a warning if no file is uploaded
   #     st.warning("No file uploaded. Please upload a CSV TNT Report.")
#else:
    # Display a message if conversion has not been done
 #    st.write(" ")

# Clean button to remove temporary files and reset the app
#if st.button("Clean"):
    # Clean up temporary files
 #   cleanup_temp_files(excel_name, uploaded_file.name)
  #  st.write("Temporary files cleaned.")
    
    # Reset the 'uploaded_file' variable to remove the file from "Browse files"
   # uploaded_file = None

    # Reset the app by clearing session state variables
    #st.session_state.clear()
