from bisect import bisect_right
from operator import contains
import re
from urllib import request
from django.shortcuts import render, redirect
import datetime
import requests
from django.http import HttpResponse
import datetime
from django.template.loader import render_to_string

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def home(request):
    cota = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
    usd = {'usd': cota['USDBRL']['low']}
    num = str(usd['usd'])
    corte = str('00.0')
    usd2 = num[:len(corte)]

    usd1 = {'usd': cota['USDBRL']['high']}
    num1 = str(usd1['usd'])
    corte1 = str('00.0')
    usd2 = num1[:len(corte1)]

    usddict_menor1 = {'usddict_menor': usd2, 'usddict': usd2}

    return render(request, 'HTML/home.html', usddict_menor1)


def dolar(request):
    cota = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
    usd = {'usd': cota['USDBRL']['bid']}
    num = str(usd['usd'])
    corte = str('00.0')
    usd2 = num[:len(corte)]
    usddict = {'usddict': usd2}
    return render(request, 'HTML/dolar.html', usddict)


def euro(request):
    cota = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
    euro = {'euro': cota['EURBRL']['bid']}
    num = str(euro['euro'])
    corte = str('00.0')
    euro2 = num[:len(corte)]
    eurodict = {'eurodict': euro2}
    return render(request, 'HTML/euro.html', eurodict)

def bitcoin(request):
    cota = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
    bitcoin = {'bitcoin': cota['BTCBRL']['bid']}
    num = str(bitcoin['bitcoin'])
    corte = str('00.0000')
    bitcoin2 = num[:len(corte)]
    bitdict = {'bitdict': bitcoin2 }
    return render(request, 'HTML/bitcoin.html', bitdict)

def dolar_maior():
    cota1 = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
    usd1 = {'usd': cota1['USDBRL']['high']}
    num1 = str(usd1['usd'])
    corte1 = str('00.0')
    usd2 = num1[:len(corte1)]
    usddict_maior = {'usddict': usd2}
    