import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

SPREADSHEET_KEY = '1gE3q5ig8XpAjr3JkzjfjKbmkwvBT_cL0XnhuxQNAXjI'

#
#  A2 : B4321 までの4320行を読んで、
#  先頭を削除し、
#  末尾に現在時刻とtemperatureを追加する
#
def update_spreadsheet(temperature):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('endless-context-225412-f7293e076fe1.json', scope)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

    import_value = worksheet.batch_get(['A2:B4321'])
    if len(import_value[0]) == 4320:
        import_value[0].pop(0)

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    import_value[0].append([now, temperature])
    export_value = {'range': 'A2:B4321', 'values': import_value[0]}

    worksheet.batch_update([export_value])


if __name__ == '__main__':
    update_spreadsheet(123)
