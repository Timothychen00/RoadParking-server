from server.models import Machine



data={
    '_id':'E01',
    'type':'esp32cam',
    'ip':'fuck',
    'status':'alive',
    'mac':'A1:B2:C3:D4',
}
Machine.edit_machine({'_id':'E01'},data)