class DataManager:
    def __init__(self):
        self.players = []
        self.nicks = set()

    def add(self, p):
        if p.nick not in self.nicks:
            self.players.append(p)
            self.nicks.add(p.nick)

    def find(self, nick):
        found = []
        for p in self.players:
            if nick.lower() in p.nick.lower():
                found.append(p)
        return found

    def get_dmg(self, p):
        return p.dmg

    def get_kills(self, p):
        return p.kills

    def get_captures(self, p):
        return p.captures

    def get_avg(self, p):
        return p.avg

    def sort(self, key):
        if key == 'dmg':
            return sorted(self.players, key=self.get_dmg, reverse=True)
        elif key == 'kills':
            return sorted(self.players, key=self.get_kills, reverse=True)
        elif key == 'captures':
            return sorted(self.players, key=self.get_captures, reverse=True)
        elif key == 'avg':
            return sorted(self.players, key=self.get_avg, reverse=True)
        else:
            return self.players