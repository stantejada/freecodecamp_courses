def add_time(start, duration, day=''):
    #splitting time duration 
    time, afte_post = start.split(' ')
    hour, minute = time.split(':') 
    days = ["monday", 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday','sunday'] #list of days
    meridiam = ['AM', 'PM'] #day or night
    dhour, dminute = duration.split(':')

    if int(dhour) > 0 and int(dhour)<=24:
        days_later = int(dhour)/24 #calculating days later
    else:
        days_later = int(dhour)/24+1 #calculating days later
    
    clock = 12
    days_count = 0
    
    total_minutes = (int(hour) * 60) + (int(dhour) * 60) + int(minute) + int(dminute) #passing whole in minutes
    new_hour = total_minutes // 60 #calculating hours
    new_minutes = total_minutes % 60 #calculating minutes
    
    auxiliary = 0
    
    if afte_post == meridiam[1]: 
        meridiam[0], meridiam[1] = meridiam[1], meridiam[0] #change a,b = b,a
    
    for turn in range((new_hour//clock)):
        if new_hour > clock:
            meridiam[0], meridiam[1] = meridiam[1], meridiam[0]
            new_hour -= clock
            days_count += 0.5
            
        elif new_hour == 12:
                meridiam[0], meridiam[1] = meridiam[1], meridiam[0]
                days_count += 0.5
                days_later+=1

        if new_minutes > 60:
            new_minutes -=60
            new_hour += 1
            
        auxiliary += 1
            
    if len(str(new_minutes)) == 1:
        new_minutes = '0'+ str(new_minutes)
         
    for d in range(len(days)):
        if day.lower() == days[d]:
            days_count += d
    
    if day!='':
        print(days_later)
        if days_count > 1 and afte_post != meridiam[0]:
            days_count +=0.5
        if int(days_count) < 1:
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0] + ', ' + days[int(days_count)].capitalize()
            return formatted
        elif int(dhour) == 24 and int(dminute)==0:
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0] + ', ' + days[int(days_count)].capitalize() + ' (next day)'
        elif int(days_count) == 1:
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0] + ', ' + days[int(days_count)].capitalize() + ' (next day)'
            return formatted
        elif int(days_count) > 1:
            days_count=days_count % 7
            if days[int(days_count)] != days[6] and days_count<6:
                days_count += 1
            
            else: 
                days_count = 0
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0] + ', ' + days[int(days_count)-1].capitalize() + f' ({int(days_later)} days later)'
            return formatted
        else:
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0] + ', ' + days[int(days_count)].capitalize()
            return formatted
    elif day=='':
        if days_count > 1 and afte_post != meridiam[0]:
            days_count +=0.5

        if int(days_count) < 1:
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0]
            return formatted
        
        if days_count == 1:
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0]  + ' (next day)'
            return formatted
        elif int(days_count) > 1:
            
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0] + f' ({int(days_count)} days later)'
            return formatted
        else:
            formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0]
            return formatted
    else:
        formatted = str(new_hour) + ':' + str(new_minutes) + ' ' + meridiam[0]
    return  formatted

print(add_time('2:59 AM', '24:00', 'saturDay'))
print('2:59 AM, Sunday (next day)')