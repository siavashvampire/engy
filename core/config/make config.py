from tinydb import TinyDB

dev = True

db = TinyDB('config.json')
db.drop_tables()
table = db.table('config')

if dev:
    table.insert({'telegram_token': "5377461148:AAFekpap_Fs-C-_3CVPi50nexYOsAQK-IuQ"})
else:
    table.insert({'telegram_token': "5712479914:AAHzQldpI9MBVl8jzcvl6m2wN3todG7rn8U"})
table.update({'admin_id': 99981475})

