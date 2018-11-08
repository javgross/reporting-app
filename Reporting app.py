
routeTime = ['Loop','Start','End','Name']
report = input()
if report != '?':
     print ('Welcome to Bluff Trail Steward Program reporting app, What is your name?')

routeTime[3] = input()
def restart():
    if routeTime[3] != '':
        print ('Alright ' + routeTime[3] + ' lets get started, what loops did you travel? ')

    garbageInfo = ['4l','3l','2l','1l']
    HA=[['4','hay marsh','fourth loop','4th','four'],
        ['3','3rd','bluff','third','three'],
        ['2','2nd','mi\'kmaq hill','second','two'],
        ['1','pot lake','first','1st','one']]
    travelAnswer = input()
    travelAnswer = travelAnswer.lower()
        
    for a in range(len(HA)):
        for e in range (len(HA[a])):
            if HA[0][e] in travelAnswer:
                routeTime[0] = '4l'
            elif HA[1][e] in travelAnswer:
                routeTime[0] = '3l'
            elif HA[2][e] in travelAnswer:
                routeTime[0] = '2l'
            elif HA[3][e] in travelAnswer:
                routeTime[0] = '1l'
        else:
            break
    for b in range(len(garbageInfo)):
        if routeTime[0] not in garbageInfo:
            routeTime[0] = travelAnswer

    print ('Ok ' + routeTime[3] + ', to the nearest hour, with am or pm, when did you start?')
    start = input()
    start = str(start.lower())
    answer = 1
    badTime = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,8,19,20,21,22,23,24]
    Time = [['1','one','1:00'],['2', 'two','2:00'],['3','three','3:00'],
          ['4','four','4:00'],['5','five','5:00'],['6','six','6:00'],
          ['7','seven','7:00am'],['8','eight','8:00'],['9','nine','9:00'],
            ['10','ten','10:00'],['11', 'eleven', '11:00'],['12','twelve','12:00']]
       

    for c in range(len(Time)):
        for d in range (len(Time[c])):
            if Time[c][d] in start:
                routeTime[1] = int(Time[c][0])
    else:
        if routeTime[1] not in badTime:
            routeTime[1] = start
            
    print ('Rad man, and, to the nearest hour, with am or pm, what time did you finish?')
    end = input()
    end = str(end.lower())
    for f in range(len(Time)): 
        for g in range (len(Time[f])):
            if Time[f][g] in end:
                routeTime[2] = int(Time[f][0])
    else:
        if routeTime[2] not in badTime:
            routeTime[2] = end
        
    if 'pm' in start:
        routeTime[1] = routeTime [1] + 12
        
    if 'pm' in end:
        routeTime[2] = routeTime[2] + 12

    error = ('did you say' + str(routeTime) + 'type restart to restart or anything else to send in das data')  
    for g in range(len(routeTime)):
        if routeTime[0] not in garbageInfo:
            print (error)
        elif routeTime[1] not in badTime:
            print (error)
        elif routeTime[2] not in badTime:
            print (error)
        else:
            if routeTime[0] in garbageInfo:
                break
            elif routeTime[1] in badTime:
                break
            elif routeTime[2] in badTime:
                break
        response = input()
        if response == 'restart':
            restart()
        if response != 'restart':
            print ('Rad I\'ll send this to my overlord')
            break
    
                            
    if routeTime[0] in garbageInfo:
        if routeTime [0] == '1l':
            print ('You did the Pot Lake loop in only '+ str(routeTime[2]-routeTime[1]) +' hours, Nice!')
        elif routeTime[0] == '2l':
            print ('You did the Pot Lake and Mi\'kmaq Hill loops in in only '+ str(routeTime[2]-routeTime[1]) +' hours, Radical man!')
        elif routeTime[0] == '3l':
            print ('You did the Pot lake, Mi\'kmaq Hill, and Bluff Loops in only '+ str(routeTime[2]-routeTime[1]) +' hours! \n Man what a trooper!')
        elif routeTime[0] == '4l':
            print ('You did the Pot lake, Mi\'kmaq Hill,Bluff, and Hay Marsh loop in only '+ str(routeTime[2]-routeTime[1]) +' hours! \n Hot dang you\'re on fire!')
        
           

restart()
