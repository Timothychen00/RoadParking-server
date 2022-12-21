from server.models import User

print(User.get_user({}))# get all users


# data={
#     '_id':'1',
#     'name':'陳澤榮',
#     'phone':'0902115275',
#     'license_plate':'EAC-8668',
#     'log':{}
# }
data={
    '_id':'2',
    'name':'陳澤榮2',
    'phone':'0902115275',
    'license_plate':'BFV3655',
    'log':{}
}


print(User.create_user(data))
# result=User.get_user({})
# print(result,len(result))



# print(User.delete_user({'name':'陳澤榮'},isSingle=False))
# result=User.get_user({})
# print(result,len(result))

