import gspread
import json

from oauth2client.service_account import ServiceAccountCredentials 

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('endless-context-225412-f7293e076fe1.json', scope)

gc = gspread.authorize(credentials)

SPREADSHEET_KEY = '1gE3q5ig8XpAjr3JkzjfjKbmkwvBT_cL0XnhuxQNAXjI'

worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

import_value = int(worksheet.acell('A1').value)

export_value = import_value+100
worksheet.update_cell(1,2, export_value)