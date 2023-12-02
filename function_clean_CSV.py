
def process_csv_file(csv_file):
    """
    Process the specified CSV file and save the result as an Excel file.

    Parameters:
    - csv_file (str): The file path of the input CSV file.

    Returns:
    - pd.DataFrame: The processed DataFrame.
    - str: The file name of the generated Excel file.
    """
    import pandas as pd
    from datetime import datetime
    import openpyxl
    
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

    # Handle the "description" column
    # Assuming your description column is named "description"
    if 'description' in csv.columns:
        csv['description'] = csv['description'].str.upper()  # Replace with your desired operation

    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Specify the desired Excel file name
    excel_name = f'TNT_Track_Report_{timestamp}.xlsx'

    # Convert DataFrame to Excel file
    csv.to_excel(excel_name, index=False)

    return csv, excel_name
