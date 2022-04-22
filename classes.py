class Television:
    """
    class representing the details for tv object.
    :param MIN_CHANNEL: Minimum TV channel.
    :param MAX_CHANNEL: Maximum TV channel.
    :param MIN_VOLUME: Minimum TV channel.
    :param MAX_VOLUME: Maximum TV channel.
    """
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    MIN_VOLUME = 0
    MAX_VOLUME = 2

    def __init__(self):
        """
        Constructor to create initial state of the tv object.
        :param Channel: private int var for tv channel set at the minimum.
        :param Volume: private int var for tv volume set at the minimum.
        :param IsOn: private boolean var for tv , set at false to be seen as off.
        """
        self.__Channel=Television.MIN_CHANNEL
        self.__Volume=Television.MIN_VOLUME
        self.__IsOn=False

    def power(self):
        """
        Method to turn the tv on or off.
        :param IsOn: turns off if it was on, turns on if it was off.
        """
        if self.__IsOn==False:
            self.__IsOn=True
        else:
            self.__IsOn=False

    def channel_up(self):
        """
        Method to change the tv channel up, won't work if the tv is off, if channel is at max(3) it will set at min(0), else it will go up one.
        :param Channel: private int var for tv channel.
        """
        if self.__IsOn==True:
            if self.__Channel<Television.MAX_CHANNEL:
                self.__Channel+=1
            else:
                self.__Channel=Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to change the tv channel down, won't work if the tv is off, if channel is at min(0) it will set at max(3), else it will go down one.
        :param Channel: private int var for tv channel.
        """
        if self.__IsOn==True:
            if self.__Channel>Television.MIN_CHANNEL:
                self.__Channel-=1
            else:
                self.__Channel=Television.MAX_CHANNEL

    def volume_up(self):
        """
        Method to change the tv volume up, won't work if the tv it off, won't go up if its at max(2)
        :param Volume: private int var for tv volume
        """
        if self.__IsOn==True:
            if self.__Volume<Television.MAX_VOLUME:
                self.__Volume+=1


    def volume_down(self):
        """
        Method to change the tv volume down, won't work if the tv is off, won't go down if its at min(0)
        :param volume: private int var for the tv volume
        """
        if self.__IsOn==True:
            if self.__Volume>Television.MIN_VOLUME:
                self.__Volume-=1



    def __str__(self):
        """
        :return: status of volume, channel, and if they tv is on/off
        """
        return f"TV status: Is on={self.__IsOn}, Channel={self.__Channel}, Volume={self.__Volume}"

