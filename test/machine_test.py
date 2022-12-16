from server.models import Machine



data={
    '_id':'E01',
    'type':'esp32cam',
    'ip':'',
    'status':'alive',
    'mac':'8:B6:1F:39:B2:FC',
}
Machine.create_machine(data)
data={
    '_id':'E02',
    'type':'esp32cam',
    'ip':'',
    'status':'alive',
    'mac':'44:17:93:7E:3B:7C',
}
Machine.create_machine(data)
data={
    '_id':'E03',
    'type':'esp32cam',
    'ip':'',
    'status':'alive',
    'mac':'8:B6:1F:39:AF:20',
}
Machine.create_machine(data)
