## Fill in the following methods for the class 'Clock'
### JDW: I got some but not all of this as we did it in lab :/


class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        #return str(self.hour) + ":" + str(self.minutes)
        return "%02d:%02d"%((self.hour % 24), (self.minutes % 60))
    
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        # modulus
        # total minutes : hrs + minutes + new minutes
        t = 60 * self.hour + self.minutes + minutes
        self.hour = t // 60
        self.minutes = t % 60
    # lol don't do this next part
    #    if self.minutes + minutes <= 60:
    #        self.minutes = self.minutes + minutes
    #    else:
    #        self.minutes = self.minutes + minutes - 60
    #        self.hour += 1
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        # self.__add__(self.minutes * -1) > 0
        t = 60 * self.hour + self.minutes - minutes
    
    ## Are two times equal?
    # Other : Clock Object
    def __eq__(self, other):
        self.hours
        other.hours
        return self.hours == other.hours and self.minutes == other.minutes

    
    ## Are two times not equal?
    def __ne__(self, other):
        return not self.__eq__(other)


# You should be able to run these
clock1 = Clock(23, 5)
print(clock1) # 23:05
clock2 = Clock(12, 45)
print(clock2) # 12:45
clock3 = Clock(12, 45)
print(clock3) # 12:45

print(clock1 == clock2) ## False
print(clock1 != clock2) ## True
print(clock2 == clock3) ## True

print("testing addition")
clock1 + 60
print(clock1) # 00:05
print(clock1 == Clock(0, 5)) # True

print("testing subtraction")
clock1 - 100
print(clock1) # 22:25