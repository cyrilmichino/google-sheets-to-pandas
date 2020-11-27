import pandas as pd


SPREADSHEET_URL = input("Enter th sheet url: ") #Example 'https://docs.google.com/spreadsheets/d/...'
RANGE_NAME = input("Enter the sheet range: ") #Example 'SheetName!A1:F101'
SPREADSHEET_ID = getsheetid(SPREADSHEET_URL)

data = getdata(SPREADSHEET_ID, RANGE_NAME)
df =  pd.DataFrame(data)
print(data)