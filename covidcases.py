import requests
from datetime import datetime
from utils import padding, humanize_date, humanize_local_date


def get_province_updates(province_id):
    url = f"https://aworkingapi.now.sh/api/v1/covid/province/{int(province_id)}"
    province = requests.get(url).json()
    improved = f'''{province["name"]}'s Covid Updates:

Tested : {padding(province["tested"])}
Positive : {padding(province["cases"])}
Recovered : {padding(province["recovered"])}
Deaths : {padding(province["deaths"])}

Updated {humanize_date(province["last_updated"])} 
    '''
    return improved


def get_today_updates(update, context):
    url = 'https://covid19.mohp.gov.np/covid/api/confirmedcases'
    updates = requests.get(url).json()["nepal"]
    improved = f'''Today's Covid Updates:

Tested : {padding(updates['today_pcr'])}
Positive : {padding(updates['today_newcase'])}
Recovered : {padding(updates['today_recovered'])}
Deaths : {padding(updates['today_death'])}

Updated {humanize_local_date(updates['updated_at'])}
'''
    update.message.reply_text(improved)


def get_local_updates(update, context):
    url = 'https://covid19.mohp.gov.np/covid/api/confirmedcases'
    updates = requests.get(url).json()["nepal"]
    improved = f'''Nepal's Covid Updates:

Tested : {padding(updates['samples_tested'])}
Positive : {padding(updates['positive'])}
Recovered : {padding(updates['extra1'])}
Deaths : {padding(updates['deaths'])}

Updated {humanize_local_date(updates['updated_at'])}
'''
    update.message.reply_text(improved)


def get_world_updates(update, context):
    url = 'https://data.nepalcorona.info/api/v1/world'
    updates = requests.get(url).json()
    improved = f'''Worldwide Covid Updates:

Tested : {padding(updates['tests'])}
Positive : {padding(updates['cases'])}
Recovered : {padding(updates['recovered'])}
Deaths : {padding(updates['deaths'])}

Updated {humanize_date(datetime.utcfromtimestamp(int(updates['updated']/1000)))}
'''
    update.message.reply_text(improved)


def get_website(update, context):
    url = "https://covidnepal.now.sh"
    update.message.reply_text(url)


def get_about(update, context):
    about = f'''Telegram bot that provides you detailed look at COVID-19 cases inside Nepal.
Web version lives at: https://covidnepal.now.sh
    
Version: 1.2.3   
Made by sidbelbase.'''
    update.message.reply_text(about)
