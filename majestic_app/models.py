from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def info(self):
        pass


class Player(Character):
    def __init__(self, nick, family, avg, dmg, kills, captures):
        self._nick = nick
        self._family = family
        self._avg = avg
        self._dmg = dmg
        self._kills = kills
        self._captures = captures

    @property
    def nick(self):
        return self._nick
    @nick.setter
    def nick(self, value):
        self._nick = value

    @property
    def family(self):
        return self._family
    @family.setter
    def family(self, value):
        self._family = value

    @property
    def avg(self):
        return self._avg
    @avg.setter
    def avg(self, value):
        self._avg = value

    @property
    def dmg(self):
        return self._dmg
    @dmg.setter
    def dmg(self, value):
        self._dmg = value

    @property
    def kills(self):
        return self._kills
    @kills.setter
    def kills(self, value):
        self._kills = value

    @property
    def captures(self):
        return self._captures
    @captures.setter
    def captures(self, value):
        self._captures = value

    def __str__(self):
        return self._nick

    def __repr__(self):
        return f'Player({self._nick})'

    def __eq__(self, other):
        return self._nick == other.nick

    def info(self):
        return self._nick