import pymongo,os
from dotenv import load_dotenv
load_dotenv()

from server.models import DB
# 如果在執行的時候是使用python -m 以模組的形式執行，在import的時候就會一直往上找，從最上層的pakage作為根目錄的起點，開始import
# 但是如果用dir/file的方式執行就會爛掉

#count_document
print(DB.db.users.count_documents({'name':1}))
