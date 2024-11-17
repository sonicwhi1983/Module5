def hour(): 
    print('Open 9-5 daily') 

    #Import it interactively: 
    import zoo 
    zoo.hour() 
#11.2 In the interaztive interpreter, import the zoo module as menagerie and call its hours() function. 
    import zoo as menagerie 
    menagerie.hour() 

    #11.3 Staynig in the interpreter, impot the hours() function from zoo directly and call it 
from zoo import hours 
hours()  

#11.4 import the hours() function as info and call it. 
from zoo import hours as info 
info() 