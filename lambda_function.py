import json


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
    result = validateJSON(event["body"])
    if result == 0:
        return {"statusCode": 200, "body": "JSON ist korrekt"}
    elif result == 2:
        return {"statusCode": 400, "body": "JSON darf nur zweidimensional sein"}
    else:
        return {"statusCode": 400, "body": "JSON ist nicht valide"}
