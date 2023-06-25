import csv
from datetime import datetime, timedelta, date
from dateutil import parser
import pandas as pd
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import StreamingHttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django import http
from requests import request
from django.db.models import Q, Sum
from django.core.paginator import Paginator
import threading
from django.http import JsonResponse
import xlwt
from django.conf import settings
from datetime import datetime
from. choice import *
from .models import *

class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def download_csv_file(col, data):
    rows = [col]
    rows.extend(data)
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=Sample_Error.csv'
    return response


def import_assortment_fn(request, dataframe):
    col = header_dict.get('assortment_error')
    cou = dataframe.shape[0]
    i = 0
    allrows = []
    while cou:
        error = []
        cou -= 1
        try:
            buyer = Buyer.objects.get(name=str(dataframe['Brand'][i]))
        except:
            error.append("Invalid Brand")
        try:
            season = Season.objects.get(name=str(dataframe['Season'][i]))
        except:
            error.append("Invalid Season")
        try:
            drop = Drop.objects.get(name=str(dataframe['Drop'][i]))
        except:
            error.append("Invalid Drop")
        try:
            gender = Gender.objects.get(name=str(dataframe['Gender'][i]))
        except:
            error.append("Invalid Gender")
        try:
            article_type = Article_Type.objects.get(name=str(dataframe['Article Type'][i]))
        except:
            error.append("Invalid Article Type")
        try:
            domimp = Domimp.objects.get(name=str(dataframe['Domestic/Import'][i]))
        except:
            error.append("Invalid Domestic/Import")
        try:
            onoff = Onoff.objects.get(name=str(dataframe['Online/Offline'][i]))
        except:
            error.append("Invalid Online/Offline")
        try:
            wwnww = Wwnww.objects.get(name=str(dataframe['WW/Nww'][i]))
        except:
            error.append("Invalid WW/Nww")
        try:
            order_type = Order_Type.objects.get(name=str(dataframe['Order Type'][i]))
        except:
            error.append("Order Type")
        try:
            fabric_type = Fabric_Type.objects.get(name=str(dataframe['Fabric Type'][i]))
        except:
            error.append("Invalid Fabric Type")

        option = str(dataframe['Option'][i])
        quantity = str(dataframe['Quantity'][i])
        today = date.today()
        if len(error):
            allrows.append([
                str(dataframe['Brand'][i]),
                str(dataframe['Season'][i]),
                str(dataframe['Drop'][i]),
                str(dataframe['Gender'][i]),
                str(dataframe['Article Type'][i]),
                str(dataframe['Domestic/Import'][i]),
                str(dataframe['Online/Offline'][i]),
                str(dataframe['WW/Nww'][i]),
                str(dataframe['Order Type'][i]),
                str(dataframe['Fabric Type'][i]),
                str(dataframe['Option'][i]),
                str(dataframe['Quantity'][i]),
                error
            ])
            i += 1
            continue
        sample = Assortment.objects.create(brand = buyer, season =season, drop=drop, gender = gender, article_type = article_type, domimp = domimp, onoff =onoff,wwnww= wwnww, order_type = order_type, fabric_type = fabric_type, options = option, quantity = quantity, assortment_date = today)
        i += 1
    response = None
    if len(allrows):
        file_name = "Assortment_error"
        response = download_csv_file(col, allrows)
    messages.success(request, 'Data Saved Successfully')
    return response

# def import_assortment_fn(request, dataframe):
#     col = header_dict.get('assortment_error')
#     cou = dataframe.shape[0]
#     i = 0
#     allrows = []
#     while cou:
#         cou -= 1
#         error = []
        
#         try:
#             season = Season.objects.get(name=str(dataframe['Season'][i]))
#         except:
#             error.append("Invalid Season")
#         try:
#             drop = Drop.objects.get(name=str(dataframe['Drop'][i]))
#         except:
#             error.append("Invalid Drop")
        
#         if len(error):
#             allrows.append([
                
                
#                 str(dataframe['Season'][i]),
#                 str(dataframe['Drop'][i]),
#                 error
#             ])
#             i += 1
#             continue
#         user = request.user.username
#         sample = None
#         rate = None
#         sample = Assortment.objects.create(season=season, drop=drop)
#         i += 1
#     response = None
#     if len(allrows):
#         response = download_csv_file(col, allrows)
#     messages.success(request, 'Data Saved Successfully')
#     return response



