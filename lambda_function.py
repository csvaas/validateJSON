import json

JSON_SUCCES = "JSON ist korrekt"
JSON_NOT_VALID = "JSON ist nicht valide"
JSON_DEPTH_ERROR = "JSON muss zweidimensional sein"


def depth(x):
    if type(x) is dict and x:
        return 1 + max(depth(x[a]) for a in x)
    if type(x) is list and x:
        return 1 + max(depth(a) for a in x)
    return 0


def validateJSON(json_str):
    # Prüfen, ob JSON korrekt ist
    error = 0
    try:
        jfile = json.loads(json_str)
    except ValueError:
        error = 1
    if error == 0:
        # Prüfen, ob JSON eine tiefe von 2 hat
        if depth(jfile) != 2:
            error = 2
    return error


def lambda_handler(event, context):
    # Ergebnis ausgeben
    result = validateJSON(event["JSON"])
    status = 200
    status_txt = JSON_SUCCES
    if result == 1:
        status = 400
        status_txt = JSON_NOT_VALID
    elif result == 2:
        status = 400
        status_txt = JSON_DEPTH_ERROR

    # AWS CloudWatch Logging
    print(status)
    print(status_txt)

    return {"statusCode": status, "statusTxt": status_txt}
