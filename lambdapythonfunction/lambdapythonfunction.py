def send(msg, status=200):
    return {
            "statusCode": status,
            "headers": {
                "Content-Type": "text/html"
                },
            "body": msg
            }

def lambdapythonfunction(event, context):
    return send("Hello world !")

