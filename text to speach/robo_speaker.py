import pyttsx3
def save_file(rate,text,voice,Name):
    Name=Name+".mp3"
    engine = pyttsx3.init() 
    #rate = engine.getProperty('rate')   
    engine.setProperty('rate', rate)

    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[voice].id)   #changing index, changes voices. 1 for female
    
    
    engine.save_to_file(text,Name)
    engine.runAndWait()
#save_file(125,"Agnik is a good boy",1,"Agnik")
def test_audio(rate,voice):
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[voice].id)
    engine.setProperty('rate', rate)
    engine.say("This is an example of the rate ")
    engine.runAndWait()
#test_audio(rate=100,voice=0)

