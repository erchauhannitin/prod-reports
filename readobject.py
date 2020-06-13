class Entry(object):
    def __init__(self, NAME, ID, ROLES, STATUS):
        super(Entry, self).__init__()
        self.NAME = NAME
        self.ID = ID
        self.ROLES = ROLES
        self.STATUS = STATUS
        self.entries = []

    def __str__(self):
        return self.ID + " " + self.ROLES + " " + self.STATUS

    def __repr__(self):
        return self.__str__()

entries = []
file = open('cluster.txt', 'r').readlines()
title = file.pop(0)
timeStamp = file.pop(0)
header = file.pop(0)

for line in file:
    words = line.split()
    NAME, ID, ROLES, STATUS = [i for i in words]
    entry = Entry(NAME, ID, ROLES, STATUS)
    entries.append(entry)

maxEntry = max(entries, key=lambda entry: entry.NAME)

entries.sort(key=lambda entry: entry.ID, reverse=True)
print(entries)
