from django.shortcuts import render
import requests

# Create your views here.

def show_data(request):
    r = requests.get('https://www.erebbit.com/ye_link_meri_jan_nikali_jati_hai')
    res = r.text.split(',')
    return render(request,
                  'chart/data.html',
                  {'total_posts':res[0],
                   'total_comments':res[1],
                   'total_users':res[2],
                   'recent_posts':res[3],
                   'recent_comments':res[4],
                   'recent_users':res[5],
                   'visitors':res[6]})
