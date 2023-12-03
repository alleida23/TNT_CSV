
def process_csv_file(csv_file):
    
    import os
    import pandas as pd
    from datetime import datetime
    #import openpyxl
    
    # Read CSV file
    csv = pd.read_csv(csv_file, sep=',""', header=0, encoding="utf-8", engine='python')

    # Basic cleaning example
    # Remove leading and trailing whitespaces from column names and all values in all columns
    csv.columns = csv.columns.str.strip('"')
    csv = csv.apply(lambda x: x.str.strip('"'))

    # Remove "/" from 'Shipment reference'
    csv['Shipment reference'] = csv['Shipment reference'].str.replace('/', '')

    # Convert 'Number of Packages' to integer
    csv['Number of Packages'] = csv['Number of Packages'].astype(int)

    # Convert 'Total weight' to float with 1 decimal
    csv['Total weight'] = csv['Total weight'].astype(float).round(1)

    # Convert 'Total volume' to float with 3 decimals
    csv['Total volume'] = csv['Total volume'].astype(float).round(3)

    # List of columns to capitalize
    columns_to_capitalize = ['Sender contact name', 'Sender city', 'Collection city', 'Receiver city', 'Delivery city', 'Tracking status']

    # Loop through specified columns and capitalize values
    for col in columns_to_capitalize:
        csv[col] = csv[col].str.capitalize()

    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Specify the desired Excel file name
    excel_name = f'TNT_Track_Report_{timestamp}.xlsx'

    # Convert DataFrame to Excel file
    csv.to_excel(excel_name, index=False)

    return csv, excel_name

def cleanup_temp_files(excel_path, csv_path, uploaded_file_path):
    # Delete the temporary Excel file
    if os.path.exists(excel_path):
        os.remove(excel_path)

    # Delete the temporary CSV file
    if os.path.exists(csv_path):
        os.remove(csv_path)

    # Delete the uploaded file
    if os.path.exists(uploaded_file_path):
        os.remove(uploaded_file_path)
