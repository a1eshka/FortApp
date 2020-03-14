import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
    url = 'https://fortniteapi.io/shop?lang=ru'
    headers = {'Authorization': 'f25a0ae7-6844635d-3dacd478-a8fbae98'}

    r = requests.get(url, headers=headers)
    results = r.json()["daily"]

    all_weapons = []
    for result in results:
        
        weapon_info = {
            
            'discription': result["description"],
            'icon': result["full_background"],
            'id': result["id"],
        }

        all_weapons.append(weapon_info)
    
    
    context = {'all_info': all_weapons}
    return render(request, 'fort/index.html', context)


def upcoming(request):
    url = 'https://fortniteapi.io/items/upcoming?lang=ru'
    headers = {'Authorization': 'f25a0ae7-6844635d-3dacd478-a8fbae98'}

    r = requests.get(url, headers=headers)
    results = r.json()["items"]

    all_weapons = []
    for result in results:
        
        weapon_info = {
            'discription': result["description"],
            'icon': result["images"]["full_background"]
        }

        all_weapons.append(weapon_info)
    

    context = {'all_info': all_weapons}
    return render(request, 'fort/upcoming.html', context)

def stats(request):
    return render(request, 'fort/stats.html')

def global_stats(request):
    url = ' https://fortniteapi.io/stats?account={}'
    account = request.GET.get('account')
    headers = {'Authorization': 'f25a0ae7-6844635d-3dacd478-a8fbae98'}

    res = requests.get(url.format(account), headers=headers).json()
    
    weapon_info = {
        'name': res["name"],
        'level': res["account"]["level"],
        'solo_kd' : res["global_stats"]["solo"]["kd"],
        'solo_winrate' : res["global_stats"]["solo"]["winrate"],
        'solo_placetop3' : res["global_stats"]["solo"]["placetop3"],
        'solo_placetop5' : res["global_stats"]["solo"]["placetop5"],
        'solo_placetop10' : res["global_stats"]["solo"]["placetop10"],
        'solo_kills' : res["global_stats"]["solo"]["kills"],
        'solo_matchesplayed' : res["global_stats"]["solo"]["matchesplayed"],
        'solo_score' : res["global_stats"]["solo"]["score"],
        'solo_minutesplayed' : res["global_stats"]["solo"]["minutesplayed"],
        'duo_kd' : res["global_stats"]["duo"]["kd"],
        'duo_winrate' : res["global_stats"]["duo"]["winrate"],
        'duo_placetop3' : res["global_stats"]["duo"]["placetop3"],
        'duo_placetop5' : res["global_stats"]["duo"]["placetop5"],
        'duo_placetop10' : res["global_stats"]["duo"]["placetop10"],
        'duo_kills' : res["global_stats"]["duo"]["kills"],
        'duo_matchesplayed' : res["global_stats"]["duo"]["matchesplayed"],
        'duo_score' : res["global_stats"]["duo"]["score"],
        'duo_minutesplayed' : res["global_stats"]["duo"]["minutesplayed"],
        'squad_kd' : res["global_stats"]["squad"]["kd"],
        'squad_winrate' : res["global_stats"]["squad"]["winrate"],
        'squad_placetop3' : res["global_stats"]["squad"]["placetop3"],
        'squad_placetop5' : res["global_stats"]["squad"]["placetop5"],
        'squad_placetop10' : res["global_stats"]["squad"]["placetop10"],
        'squad_kills' : res["global_stats"]["squad"]["kills"],
        'squad_matchesplayed' : res["global_stats"]["squad"]["matchesplayed"],
        'squad_score' : res["global_stats"]["squad"]["score"],
        'squad_minutesplayed' : res["global_stats"]["squad"]["minutesplayed"],

        
        
    }
    
    context = {'info': weapon_info}
    return render(request, 'fort/global_stats.html', context)


def news(request):
    url = 'https://fortniteapi.io/news?lang=ru&type=br'
    headers = {'Authorization': 'f25a0ae7-6844635d-3dacd478-a8fbae98'}

    r = requests.get(url, headers=headers)
    results = r.json()["news"]

    all_weapons = []
    for result in results:
        
        weapon_info = {
            'title': result["title"],
            'body': result["body"],
            'image': result["image"],
            
        }

        all_weapons.append(weapon_info)
    
    
    context = {'all_info': all_weapons}
    return render(request, 'fort/news.html', context)

def find_id(request):
    return render(request, 'fort/find_id.html')


def your_id(request):
    url = 'https://fortniteapi.io/lookup?username={}'
    username = request.GET.get('username')
    headers = {'Authorization': 'f25a0ae7-6844635d-3dacd478-a8fbae98'}

    res = requests.get(url.format(username), headers=headers).json()
    
    weapon_info = {
        'account_id': res["account_id"],
    }
    
    context = {'info': weapon_info}
    return render(request, 'fort/your_id.html', context)

def weapon_detail(request):
    url = ' https://fortniteapi.io/items/get?id={}&lang=ru'
    headers = {'Authorization': 'f25a0ae7-6844635d-3dacd478-a8fbae98'}
    id = request.GET.get('id')
    res = requests.get(url.format(id), headers=headers).json()
    
    weapon_info = {
        'description': res["item"]["description"],
        'id': res["item"]["id"],
        'images': res["item"]["images"]["full_background"],
        'interest': res["item"]["interest"],
        'rarity': res["item"]["rarity"],
        'releaseDate': res["item"]["releaseDate"],
        'set': res["item"]["set"],
        'name': res["item"]["name"],
        'price': res["item"]["price"],
        
    }
    context = {'info': weapon_info}
    return render(request, 'fort/weapon_detail.html', context)

def events(request):
    url = 'https://fortniteapi.io/events/list'
    headers = {'Authorization': 'f25a0ae7-6844635d-3dacd478-a8fbae98'}

    r = requests.get(url, headers=headers)
    results = r.json()["events"]

    all_weapons = []
    for result in results:
        
        weapon_info = {
        'long_description': result["short_description"],
        'name_line1': result["name_line1"],
        'name_line2': result["name_line2"],
        'platforms': result["platforms"],
        'poster': result["poster"],
        'schedule': result["schedule"],
            
        }

        all_weapons.append(weapon_info)
    
    
    context = {'all_info': all_weapons}
    return render(request, 'fort/events.html', context)