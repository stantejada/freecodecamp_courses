def add_time(start, duration, day=''):

    time, afte_post = start.split(' ')
    hour, minute = time.split(':')
    days = ["monday", 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday','sunday']
    meridiam = ['AM', 'PM']
    dhour, dminute = duration.split(':')

    
    
    clock = 12
    change=0
    days_count = 0
    
    total_minutes = (int(hour) * 60) + (int(dhour) * 60) + int(minute) + int(dminute)
    new_hour = total_minutes // 60
    new_minutes = total_minutes % 60
    
    if afte_post == meridiam[1]:
        meridiam[0], meridiam[1] = meridiam[1], meridiam[0]
    
    for turn in range((new_hour//clock)):
        if new_hour > clock:
            meridiam[0], meridiam[1] = meridiam[1], meridiam[0]
            new_hour -= clock
            days_count += 0.5
            
        elif new_hour == 12:
                meridiam[0], meridiam[1] = meridiam[1], meridiam[0]
                days_count += 0.5

        if new_minutes > 60:
            new_minutes -=60
            new_hour += 1

            
    if len(str(new_minutes)) == 1:
        new_minutes = '0'+ str(new_minutes)
         
    for d in range(len(days)):
        if day.lower() == days[d]:
            days_count += d
    
    if day!='':
        if int(days_count) <= 1:
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0] + ', ' + days[int(days_count)+1].capitalize() + ' (next day)'
        elif int(days_count) > 1:
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0] + ', ' + days[int(days_count)+1].capitalize() + f' ({int(days_count)} days later)'
        formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0] + ', ' + days[int(days_count)+1].capitalize()
    
    else:
        formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0]
    return  formatted
print(add_time('11:59 PM', '0:10'))


