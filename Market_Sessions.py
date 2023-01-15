from time import time
import jdatetime,time

                                                                        ### Function for Market session ###
def Market_Sessions(y = jdatetime.datetime.now()):
    l =[]
    if y.strftime('%A') in ('saturday','sonday'):
        x = 'market close'
        print (x)
    else:
        x = 'market open'
        
        ####Check london time##
        if 11 <= int(y.strftime('%H')) <= 19:
            if int(y.strftime('%H')) == 11 :
                if int(y.strftime('%M')) >= 30:
                    l.append('london')
                
            elif int(y.strftime('%H')) == 19 :
                if int(y.strftime('%M')) <= 30:
                    l.append('london') 
            else:
                l.append('london')
                pass
            pass
        
        ####  Check NYC time ##
        if int(y.strftime('%H')) >= 18 or int(y.strftime('%H')) == 0 :              
            if int(y.strftime('%H')) == 0 :
                if int(y.strftime('%M')) <= 30:
                    l.append('NYC')

            else:
                l.append('NYC')
                pass
            pass
        
        #### Check Tokyo time##
        if 3 <= int(y.strftime('%H')) <= 11:
            if int(y.strftime('%H')) == 3 :
                if int(y.strftime('%M')) >= 30:
                    l.append('Tokyo')
                
            elif int(y.strftime('%H')) == 11 :
                if int(y.strftime('%M')) <= 30:
                    l.append('Tokyo')
            else:
                l.append('Tokyo')
                pass
            pass
        
        ####Check Berlin time##
        if 10 <= int(y.strftime('%H')) <= 18:
            if int(y.strftime('%H')) == 10 :
                if int(y.strftime('%M')) >= 30:
                    l.append('Berlin')
                
            elif int(y.strftime('%H')) == 18 :
                if int(y.strftime('%M')) <= 30:
                    l.append('Berlin')
            
            else:
                l.append('Berlin')
                pass
            pass
        
        ####Check Sydney time##
        if 2 <= int(y.strftime('%H')) <= 10:
            if int(y.strftime('%H')) == 2 :
                if int(y.strftime('%M')) >= 30:
                    l.append('Sydney')
                
            elif int(y.strftime('%H')) == 10 :
                if int(y.strftime('%M')) <= 30:
                    l.append('Sydney')
            
            else:
                l.append('Sydney')
                pass
            pass
        if len(l) > 0 :
            
            print('The sessions which open is :')
            for i in l :
                print('+-->', i, '<--+')
                pass
        else:
            print("i don't section which be open ")    
    pass

                                                                        ### Function for Date ###   
def Date(y = jdatetime.datetime.now().date()):
    print(
        'Today is {} \n    {}/{}/{} '.format(
            y.strftime('%A'), y.strftime('%Y'), y.strftime('%m'), y.strftime('%d')
            )
        )
    pass

                                                                        ### Function for Time ###
def Time(y = jdatetime.datetime.now().time().strftime('%H:%M')):
    print(y)
    pass



###################### OUT ######################
Market_Sessions()
Date()
Time()
