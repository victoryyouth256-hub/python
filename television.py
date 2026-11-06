class Television:
    """
    Class representing a television with power, mute, channel, and volume controls.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Constructor to create the initial state of a Television object.
        The tv starts off, unmuted, on the minimum volume and the minimum channel.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn the tv on and off by toggling the value of the status variable.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to mute and unmute the tv by toggling the muted variable.
        Only works when the tv is on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase the tv channel by one when the tv is on.
        If the tv is on the maximum channel, the channel wraps around to the minimum channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel by one when the tv is on.
        If the tv is on the minimum channel, the channel wraps around to the maximum channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the tv volume by one when the tv is on.
        If the tv is muted, it is automatically unmuted first.
        If the tv is on the maximum volume, the volume remains at the maximum.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume by one when the tv is on.
        If the tv is muted, it is automatically unmuted first.
        If the tv is on the minimum volume, the volume remains at the minimum.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to return the current state of the tv as a string.
        When the tv is muted, the volume is displayed as the minimum volume.
        :return: String in the format Power = [status], Channel = [channel], Volume = [volume]
        """
        if self.__muted:
            volume: int = Television.MIN_VOLUME
        else:
            volume = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
