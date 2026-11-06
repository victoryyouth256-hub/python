import pytest
from television import Television


class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        # tv on
        self.tv.power()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
        # tv off
        self.tv.power()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        # tv on, volume increased once, then muted
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
        # tv on and unmuted
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # tv off and unmuted (mute has no effect when off)
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'
        # tv off and muted: mute while on, power off, then mute() must not unmute it
        self.tv.power()
        self.tv.mute()
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_up(self):
        # tv off and channel increased
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # tv on and channel increased
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 1, Volume = 0'
        # tv on and channel increased past the maximum value
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        # tv off and channel decreased
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # tv on and channel decreased past the minimum value
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        # tv off and volume increased
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # tv on and volume increased
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # tv on, muted, and volume increased
        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'
        # tv on and volume increased past the maximum value
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        # tv off and volume decreased
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # tv on and volume decreased (volume raised to the maximum first)
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # tv on, muted, and volume decreased (start at the maximum so unmuting is observable)
        self.tv.volume_up()
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # tv on and volume decreased past the minimum value
        self.tv.volume_down()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
