import re

def getsheetid(url):
      "Get the document unique ID from the the unique document url"
  
  #clear out all the domain details
  sheet_id = str(re.findall("https://docs.google.com/spreadsheets/d/(.+)", url)[0])

  #remove url queries from unique id
  if "/" in sheet_id:
    return str(re.findall("(.+)/.+", sheet_id)[0])
  
  #return id if sheet_id has no queries
  else:
    return sheet_id