# Google Sheets to Python Pandas
### Import data from Google Sheets into a Python Pandas dataframe.
 
These python scripts are meant for Data Scientists looking to import CSV/XLSX data directly from Google Sheets rather than downloading the files and importing into your project Jupyter Notebook. You can copy paste the code in the files into your notebook in the following order:

| File Name | Comment out the following lines of code on Jupyter Notebooks |
|---|---|
| getsheetID.py |
| getsheetdata.py | ```from googlesheetID import getsheetid``` |
| main.py | ```from getsheetID import getdata``` |

## Instructions
1. Create your Google Sheets API credentials from your [Google Developer Console](https://console.developers.google.com/)
2. Download your credentials file and save it in the repository as **credentials.json**
3. You can now run the **main.py** file to import data from sheets into a pandas dataframe

For additional instructions on how to work with Google Sheets APIs, visit [Google Sheets API – Python Quickstart](https://developers.google.com/sheets/api/quickstart/python)

## Acknowledgements
Part of this repository contains code modified from [Google Developer Site](https://developers.google.com/sheets/api/quickstart/python)
