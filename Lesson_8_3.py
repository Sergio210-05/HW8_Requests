import requests
import datetime
from pprint import pprint


def unix_date(date):
    days = date - datetime.date(1970, 1, 1)
    unix_date = days.days * 24 * 3600
    return unix_date


def get_response(today_date, days_before_today, tag='python'):
    fromdate = today_date - datetime.timedelta(days=days_before_today)
    unix_today = unix_date(today_date)
    unix_fromdate = unix_date(fromdate)
    url = f'https://api.stackexchange.com/2.3/questions?fromdate={unix_fromdate}' \
          f'&todate={unix_today}&order=desc&sort=activity&tagged={tag}&site=stackoverflow'
    response = requests.get(url=url)
    print('Request status:', response.status_code)
    return response


def title_link(response_json):
    for item in response_json['items']:
        print(item['title'], ':', sep='')
        print(item['link'])


if __name__ == '__main__':
    todate = datetime.datetime.today().date()
    response = get_response(todate, 2, tag='python')
    # pprint(response.json())
    title_link(response.json())
