def clean_CSV_file(csv_file):
    """
    Cleans and processes the specified CSV file and saves the result as an Excel file.

    Parameters:
    - input_csv_path (str): The file path of the input CSV file.

    Returns:
    None
    """
    
    import pandas as pd
    from datetime import datetime
    
    # Read CSV File
    csv = pd.read_csv(csv, sep=r',""', header=0, encoding="utf-8", engine='python')

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
        csv[col] = csv[col].str.capitalize()

    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Specify the desired Excel file name
    output_excel_file = f'TNT_Track_Report_{timestamp}.xlsx'
    
    return csv, output_excel_file

    # Convert DataFrame to Excel file
    #csv.to_excel(output_excel_file, index=False)

    #print(f"DataFrame has been successfully converted and saved as Excel file: {output_excel_file}")

# Example usage
#clean_CSV_file('myTNT_2023_11_30_07_46.csv')
