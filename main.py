import requests
import json
import xmltodict

from flask import Flask

def get_valutes_list():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = xmltodict.parse(requests.get(url).text)
    valutes = response['ValCurs']
    valutes = list(valutes["Valute"])
    return valutes

get_valutes_list()


app = Flask(__name__)


def create_html(valutes):
    text = '<h1>Курс валют</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()