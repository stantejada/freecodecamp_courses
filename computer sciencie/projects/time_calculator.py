def add_time(start, duration, day=''):

    time, afte_post = start.split(' ')
    hour, minute = time.split(':')
    days = ["lunes", 'martes', 'miercoles', 'jueves', 'viernes', 'sabado','domingo']
    meridiam = ['AM', 'PM']
    dhour, dminute = duration.split(':')

    
    
    clock = 12
    change=0
    days_count = 0
    
    total_minutes = (int(hour) * 60) + (int(dhour) * 60) + int(minute) + int(dminute)
    new_hour = total_minutes // 60
    new_minutes = total_minutes % 60
    
    for turn in range(new_hour//clock):
        if new_hour > clock:
           # meridiam[0], meridiam[1] = meridiam[1], meridiam[0]
            new_hour -= clock
            print(meridiam[0])
        elif new_hour < clock:
            break
        if new_minutes > 60:
            new_minutes -=60
            new_hour += 1
        
    

    return  new_hour, new_minutes , (total_minutes//60) ,':' ,(total_minutes%60)


print(add_time('11:59 AM', '24:10'))

meridiam = ['AM', 'PM']

print(meridiam.index('AM'))