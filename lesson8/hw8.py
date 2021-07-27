from datetime import datetime, timedelta
from collections import defaultdict


users = [{'name':'Jack', 'birthday':'01-05-90'},
        {'name':'John', 'birthday':'29-07-90'},
        {'name':'Ella', 'birthday':'30-07-90'},
        {'name':'Fiji', 'birthday':'24-07-90'},
        {'name':'Kate', 'birthday':'26-07-90'},
        {'name':'Mike', 'birthday':'25-07-90'},
        {'name':'Bill', 'birthday':'27-07-90'},
        {'name':'Eve', 'birthday':'01-08-90'},
        {'name':'Jane', 'birthday':'01-08-90'},
        {'name':'Heather', 'birthday':'24-07-90'},
        {'name':'Brandon', 'birthday':'28-07-90'},
        {'name':'Bruce', 'birthday':'29-07-90'}]


def congratulate(users):
    
    now = datetime.today()
    saturday_days_ago = timedelta(now.weekday()+2)
    days_this_week_list = [now - saturday_days_ago + timedelta(i) for i in range(7)]
    days_this_week_tuple_dict = {(i.month, i.day): i.strftime('%A') for i in days_this_week_list}
    result_list_dict = defaultdict(list)

    for i in users:
        month_day = (datetime.strptime((i['birthday']), '%d-%m-%y').month, 
                    datetime.strptime((i['birthday']), '%d-%m-%y').day)
        if month_day in days_this_week_tuple_dict:
            result_list_dict[days_this_week_tuple_dict[month_day]].append(i['name'])

    result_list_dict['Monday'].extend(
        result_list_dict['Saturday'] + result_list_dict['Sunday'])
    del result_list_dict['Saturday'], result_list_dict['Sunday']

    print(f"""Monday:    {(', '.join(result_list_dict['Monday']))}
Tuesday:   {', '.join(result_list_dict['Tuesday'])}
Wednesday: {', '.join(result_list_dict['Wednesday'])}
Thursday:  {', '.join(result_list_dict['Thursday'])}
Friday:    {', '.join(result_list_dict['Friday'])}""")


def main():
    congratulate(users)


if __name__ == '__main__':
    main()
