from dotenv import load_dotenv
import pymongo,os,datetime
load_dotenv()

# isSingle True  =1
# ISingle False  >=1

class DB():
    client=pymongo.MongoClient("mongodb+srv://admin:"+os.environ['DB_PASS']+"@roadparking.zgcphsq.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
    db=client.RoadParking

def check_document(collection='users',key_value={},isSingle:bool=True):# 返回值都是err的錯誤
    '''
    to do a simple check of all the files in the databse
    '''
    print(key_value)
    if len(key_value) or not isSingle:
        counts=DB.db[collection].count_documents(key_value)
        if counts==0:
            return {'err':'not found'}
        # >0
        if isSingle:
            if counts>1:
                return {'err':'too many results'}
        return {'err':None}
    return {'err':'key and value are required for checking documents'}

class Parking:
    def create_parking(args:dict):
        data = {
            '_id' : "",
            'status' : "", # empty or inuse 
            'position':[],
            'license_plate' : "",
            'machine' : ""
        }
        
        for key in data:
            if key in args:
                data[key]=args[key]
        if 'position_x' in args and 'position_y' in args:
            data['position']=[args['position_x'],args['position_y']]
        print(data)
        result=DB.db['parking'].insert_one(data)
        return {'data':data}
        

    def delete_parking(key_value:dict,isSingle=True):
        result = check_document('parking',key_value,isSingle)
        if not result['err']:
            if isSingle:
                DB.db['parking'].delete_one(key_value)
            else:
                DB.db['parking'].delete_many(key_value)
            return 'deleted'
        return result['err']
    
    def edit_parking(key_value:dict,data,overwrite=False):
        result = check_document('parking',key_value,isSingle=True)
        if not result['err']:
            if not overwrite:
                if 'status' in data:
                    result=DB.db['parking'].find_one(key_value)
                    if result['status']!=data['status']:#有需要更新 車位的狀態不一樣      data    status license_plate
                        print(data)
                        print(data['license_plate'])
                        user=User.get_user({'license_plate':data['license_plate']})[0]
                        print(user)
                        log=user['log']
                        month,day,now_time=get_date()
                        if data['status']=='empty':#離開，準備更新時間的部分
                            if not month in log:
                                return '請先將車停入'
                            if not day in log[month]:
                                return '請先將車停入'
                            log[month][day]['out']=now_time
                            
                            d1=datetime.datetime.strptime(log[month][day]['in'],"%H:%M:%S")
                            d2=datetime.datetime.strptime(log[month][day]['out'],"%H:%M:%S")
                            log[month][day]['duration']=[(d2-d1).seconds//3600,((d2-d1).seconds//60)%60]
                            
                            log[month][day]['fee']=log[month][day]['duration'][0]*30
                            if log[month][day]['duration'][1]>0:
                                log[month][day]['fee']+=30
                            
                            # return '記錄完成'
                            Parking.edit_parking(key_value,{'status':'empty'},overwrite=True)

                        else:#開始記錄時間
                            if not month in log:
                                log[month]={}

                            log[month][day]={'in':'0:0:0','out':'0:0:0','duration':[0,0],'fee':'0','status':'0'}
                            log[month][day]['in']=now_time
                            # log[]
                            Parking.edit_parking(key_value,{'status':'inuse'},overwrite=True)
                        User.edit_user({'license_plate':data['license_plate']},{'log':log})
                        return 'done'
                    else:
                        return 'non chanegd'
            DB.db['parking'].update_one(key_value,{'$set':data})
            return 'edit successfully'
        return result['err']
    
    # def park_parking(key_value:dict,data):
    #     pass
    
    
    def get_parking(key_value:dict,isSingle=False):
        result = check_document('parking',key_value,isSingle)
        if not result['err']:
            data=DB.db['parking'].find(key_value)
            return list(data)
        
        if result['err']=='not found':
            return []
        return result['err']
    

class Machine:
    def create_machine(args:dict):
        data={
            '_id':'',
            'type':'',
            'status':'',
            'ip':'',
            'mac':'',
        }
        print(args)
        
        for key in data:
            if key in args:
                print(key)
                data[key]=args[key]
        print(data)
        result=DB.db['machine'].insert_one(data)
        return {'data':data}
    
    def delete_machine(key_value:dict,isSingle=True):
        result = check_document('machine',key_value,isSingle)
        if not result['err']:
            if isSingle:
                DB.db['machine'].delete_one(key_value)
            else:
                DB.db['parking'].delete_many(key_value)
            return 'deleted'
        return result['err']
    
    def edit_machine(key_value:dict,data):
        result = check_document('machine',key_value,isSingle=True)
        if not result['err']:
            DB.db['machine'].update_one(key_value,{'$set':data})
            return 'edit successfully'
        return result['err']
        
    def get_machine(key_value,isSingle=False):
        result = check_document('machine',key_value,isSingle)
        if not result['err']:
            data=DB.db['machine'].find(key_value)
            return list(data)
        
        if result['err']=='not found':
            return []
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
        result=DB.db['users'].insert_one(data)
        return {'data':data}
    
    def delete_user(key_value:dict,isSingle=True):
        result = check_document('users',key_value,isSingle=isSingle)
        if not result['err']:
            if isSingle:
                DB.db['users'].delete_one(key_value)
            else:
                DB.db['users'].delete_many(key_value)
            return 'deleted'
        return result['err']

    def edit_user(key_value,data):
        result = check_document('users',key_value,isSingle=True)
        if not result['err']:
            DB.db['users'].update_one(key_value,{'$set':data})
            return 'edit successfully'
        return result['err']
    
    def get_user(key_value,isSingle=False):
        result = check_document('users',key_value,isSingle)
        if not result['err']:
            data=DB.db['users'].find(key_value)
            return list(data)
        
        if result['err']=='not found':
            return []
        return result['err']


def get_date(date=None):
    '''return(month,date,time)'''
    print(date)
    if not date:
        date=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y-%m-%d %H:%M:%S")
    if ' 'in date:
        time=date.split()[1]
        day=date.split()[0]
    else:
        time=None
        day=date
    month="-".join(day.split('-')[:-1])
    return (month,day,time)