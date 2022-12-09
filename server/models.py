from flask_restful import Resource, reqparse
from dotenv import load_dotenv
import pymongo,os
load_dotenv()

class DB():
    client=pymongo.MongoClient("mongodb+srv://admin:"+os.environ['DB_PASS']+"@roadparking.zgcphsq.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
    db=client.RoadParking

def check_document(key_value,isSingle:bool=True):# 返回值都是err的錯誤
    '''
    to do a simple check of all the files in the databse
    '''
    if len(key_value) or not isSingle:
        counts=DB.db.users.count_documents(key_value)
        if counts==0:
            return {'err':'not found'}
        # >0
        if isSingle:
            if counts>1:
                return {'err':'too many results'}
        return {'err':None}
    return {'err':'key and value are required for checking documents'}

# class Parking:
    
#     def post(self):
#         args = self.parser.parse_args()
#         data={
#             'spaceid':args['spaceid'],
#             'stats':args['stats'],
#             'license_plate':args['license_plate'],
#         }
#         result=DB.db.users.insert_one(data)
#         return {'已添加的id':result.inserted_id}
    
#     def delete(self):
#         pass
#     def put(self):
#         pass
#     def get(self):
#         pass

class Machine:
    def create_machine(args:dict):
        data={
            '_id':'',
            'type':'',
            'status':'',
            'postion':[],#position in args is parse to position_x and position_y
            'ip':'',
            'mac':'',
        }
        for key in data:
            if key in data:
                data[key]=args[key]
            if 'position_x' in args and 'position_y' in args:
                data['position']=[args['position_x'],args['position_y']]
        print(data)
        result=DB.db.machine.insert_one(data)
        return {'data':data}
    
    def delete_user(key_value:dict,isSingle=True):
        result = check_document(key_value,isSingle)
        if not result['err']:
            if isSingle:
                DB.db.machine.delete_one(key_value)
            else:
                DB.db.machine.delete_many(key_value)
            return 'deleted'
        return result['err']
    
    def edit_machine(key_value:dict,data):
        result = check_document(key_value,isSingle=True)
        if not result['err']:
            DB.db.users.update_one(key_value,{'$set':data})
            return 'edit successfully'
        return result['err']
        
    def get_machine(key_value,isSingle=False):
        result = check_document(key_value,isSingle)
        if not result['err']:
            data=DB.db.users.find(key_value)
            return list(data)
        return result['err']


class User:
    def create_user(args:dict):
        data={
            '_id':'',
            'name':'',
            'phone':'',
            'license_plate':'',
            'log':{}
        }
        for key in data:
            if key in args:
                data[key]=args[key]
        print(data)
        result=DB.db.users.insert_one(data)
        return {'data':data}
    
    def delete_user(key_value:dict,isSingle=True):
        result = check_document(key_value,isSingle=isSingle)
        if not result['err']:
            if isSingle:
                DB.db.users.delete_one(key_value)
            else:
                DB.db.users.delete_many(key_value)
            return 'deleted'
        return result['err']

    def edit_user(key_value,data):
        result = check_document(key_value,isSingle=True)
        if not result['err']:
            DB.db.users.update_one(key_value,{'$set':data})
            return 'edit successfully'
        return result['err']
    
    def get_user(key_value,isSingle=False):
        result = check_document(key_value,isSingle)
        if not result['err']:
            data=DB.db.users.find(key_value)
            return list(data)
        return result['err']
