
from flask_restful import Resource,reqparse
from server.models import User,Machine
from flask import jsonify

# need DB schema and User data schema

class UserAPI(Resource):
    parser=reqparse.RequestParser()
    # use for addition requirements(put,get,post)
    parser.add_argument('name',type=str,location=['values'])
    parser.add_argument('phone',type=str,location=['values'])
    parser.add_argument('license_plate',type=str,location=['values'])
    # use for search
    parser.add_argument('key',type=str,location=['values'])
    parser.add_argument('value',type=str,location=['values'])
    
    def post(self):
        args = self.parser.parse_args()
        result = User.create_user(args)
        return result
    
    def delete(self):   
        args = self.parser.parse_args()
        result = User.delete_user({args['key']:args['value']})
        return result
        
    def put(self):
        args = self.parser.parse_args()
        data={}
        for i in ['name','phone','license_plate']:
            data[i]=args[i]
            
        result = User.edit_user({args['key']:args['value']},data)
            
        return result
    
    def get(self):# not limited to single document
        args = self.parser.parse_args()
        result = User.get_user({args['key']:args['value']})
        return result

class ParkingAPI(Resource):
    pass
#     parser=reqparse.RequestParser()
#     parser.add_argument('spaceid',type=str,location=['values'])
#     parser.add_argument('license_plate',type=str,location=['values'])
#     parser.add_argument('stats',type=str,location=['values'])
    
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
    
class MachineAPI(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('_id',type=str,location=['values'])
    parser.add_argument('type',type=str,location=['values'])
    parser.add_argument('status',type=str,location=['values'])
    parser.add_argument('position_x',type=str,location=['values'])
    parser.add_argument('position_y',type=str,location=['values'])
    parser.add_argument('ip',type=str,location=['values'])
    parser.add_argument('mac',type=str,location=['values'])
    # use for search
    parser.add_argument('key',type=str,location=['values'])
    parser.add_argument('value',type=str,location=['values'])
    
    def post(self):
        args = self.parser.parse_args()
        result = Machine.create_machine(args)
        return result

    def delete(self):
        args = self.parser.parse_args()
        result=Machine.delete_machine({args['key']:args['value']})
        return result
        
    def put(self):
        args = self.parser.parse_args()
        data={}
        for i in ['type','status','position_x','position_y','ip','mac']:
            data[i]=args[i]

        result = Machine.edit_machine({args['key']:args['value']},data)
        return result
        
    def get(self):
        args = self.parser.parse_args()
        
        filter = {}
        print(2)
        if args['key']:
            print(1)
            filter = {args['key']:args['value']}
        result = Machine.get_machine(filter)
        print(result)
        return result
