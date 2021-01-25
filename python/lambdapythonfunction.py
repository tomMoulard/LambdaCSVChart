import urllib.request
import urllib.parse
from os import path
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(path.join(path.dirname(__file__), 'templates'), encoding='utf8'))

def send(msg, status=200):
    return {
            "statusCode": status,
            "headers": {
                "Content-Type": "text/html"
                },
            "body": msg
            }


def err(msg):
    return send(msg, 500)


def ok(msg):
    return send(msg)


def html(url, size):
    f = urllib.request.urlopen(url)
    csv = f.read().decode('utf-8')
    template = env.get_template('index.html', )
    return ok(template.render(csv="\n".join(csv.split("\n")[:size]), size=size))


def lambdapythonfunction(event, context):
    try:
        url = event['queryStringParameters']['url']
        size = event['queryStringParameters']['size']
    except:
        template = env.get_template('error.html', )
        return err(template.render())
    return html(url, size)


if __name__ == "__main__":
    #  print(lambdapythonfunction("https://pi.moulard.org/speedtest/cronSpeedtest-cli.csv", -1))
    print(html("https://pi.moulard.org/speedtest/cronSpeedtest-cli.csv", 2))
