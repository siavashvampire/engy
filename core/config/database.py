from typing import Union

from tinydb import TinyDB, Query

db = TinyDB('core/config/config.json')
query = Query()
table = db.table('config')

data = table.all()
data_all = None

if len(data):
    data_all = data[0]
else:
    raise ValueError('config database not set!please run make config!!')

telegram_token: str = data_all['telegram_token']
admin_id: int = data_all['admin_id']


def update_database(key: str, value: Union[int, float]) -> None:
    table.update({key: value})


def get_database(key: str):
    return data_all[key]