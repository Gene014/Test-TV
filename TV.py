#Calma, Eugene Marie S.

# transferring uml diagram into text (serves as my guide)

#tv1's channel is 30 and volume level is 3 
#tv2's channel is 3 and volume level is 2 
#channel: int 
#volumeLevel: int 
#on: bool 




#getVolume (): int

#channe1Up(): None
#channelDown (): None
#volumeUp(): None
#volumeDown (): None
#The current channel (1 to 120) of this TV. 
#The current volume level (1 to 7) of this TV. 
#Indicates whether this TV is on/off. 
#Constructs a default TV object.  
#Turns on this TV.  
#Turns off this TV.    
#Returns the channel for this TV. 
#Sets a new channel for this TV. 
#Gets the volume level for this TV. 
#Sets a new volume level for this TV. 
#Increases the channel number by 1. 
#Decreases the channel number by 1. 
#Increases the volume level by 1. 
#Decreases the volume level by 1.      

#Creating Pseudocode
#Generating Class

# TV()
class TV:
    def ___init___(self):
        self.channel= 1
        self.volumeLevel= 1
        self.on= False
        # turnOn (): None
    def turnOn(self):
        self.on=True
        # turnOff(): None
    def turnOff(self):
        self.on=False
        # getChannel(): int
    def getChannel(self):
        return self.channel
        #setChannel (channel: int): None
    def setChannel(self,num):
        if num>=1 and num<=120:
            self.channel=num
        #getVolume (): int
    def getVolume(self):
        return self.volumeLevel
        #setVolume (volume Level: int): None
    def setVolume(self,volumelevel):
        if volumelevel>=1 and volumelevel<=7:
            self.volumeLevel=volumelevel 
                   
#Creating Constructor
#Creating Instances
#Call Methods