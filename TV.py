#Calma, Eugene Marie S.

# transferring uml diagram into text (serves as my guide)

#tv1's channel is 30 and volume level is 3 
#tv2's channel is 3 and volume level is 2 
#channel: int 
#volumeLevel: int 
#on: bool 


#Creating Pseudocode
#Generating Class
#Creating Constructor
#Creating Instances

# TV()
class TV:
            #The current volume level (1 to 7) of this TV. 
            #Indicates whether this TV is on/off. 
            #Constructs a default TV object.  
    def ___init___(self):
        self.channel= 1
        self.volumeLevel= 1
        self.on= False
            #Turns on this TV. 
            # turnOn (): None
    def turnOn(self):
        self.on=True
            #Turns off this TV.
            # turnOff(): None
    def turnOff(self):
        self.on=False
            #Returns the channel for this TV. 
            # getChannel(): int
    def getChannel(self):
        return self.channel
            #Sets a new channel for this TV.
            #setChannel (channel: int): None
    def setChannel(self,num):
        if num>=1 and num<=120:
            self.channel=num
            #Gets the volume level for this TV. 
            #getVolume (): int
    def getVolume(self):
        return self.volumeLevel
            #Sets a new volume level for this TV. 
            #setVolume (volume Level: int): None
    def setVolume(self,volumelevel):
        if volumelevel>=1 and volumelevel<=7:
            self.volumeLevel=volumelevel 
            #Increases the channel number by 1. 
            #channe1Up(): None 
    def channelUp(self):
        if self.channel<120:
            self.channel+=1
        else:
            self.channel=1
            #Decreases the channel number by 1. 
            #channelDown (): None
    def channelDown(self):
        if self.channel>1:
            self.channel-=1
        else:
            self.channel=120
            #Increases the volume level by 1. 
            #volumeUp(): None
    def volumelUp(self):
        if self.channel<7:
            self.channel+=1
        else:
            self.channel=1
            #Decreases the volume level by 1.  
            #volumeDown (): None
    def volumeDown(self):
        if self.channel>1:
            self.channel-=1
        else:
            self.channel=7

#Call Methods
#call methods to main program