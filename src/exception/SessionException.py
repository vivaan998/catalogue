
def NotFound(sessionUUID, ex):
    exc = dict()
    exc['errors'] = [{
        "code" : 404,
        "message" : "No data found for UUID: " + sessionUUID
    }]
    return exc

def GeneralException(ex):
    exc = dict()
    exc['errors'] = [{
        "code" : 403,
        "message" : str(ex)
    }]
    return exc

def SessionUUIDNotGiven():
    exc = dict()
    exc['errors'] = [{
        "code" : 404,
        "message" : "Session UUID not parsed"
    }]
    return exc
