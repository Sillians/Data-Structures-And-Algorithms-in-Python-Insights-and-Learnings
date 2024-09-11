# P-2.35
# Write a set of Python classes that can simulate an Internet application in which one party,
# Alice, is periodically creating a set of packets that she wants to send to Bob.
# An Internet process is continually checking if Alice has any packets to send, and if so,
# it delivers them to Bob’s computer, and Bob is periodically checking if his computer has a packet from Alice,
# and, if so, he reads and deletes it.


import random

class AliceApplication:
    ODDS_OF_ACTING = 0.5
    def __init__(self):
        self._current_packet = None

    def act(self):
        if random.random()<=self.ODDS_OF_ACTING:
            self._current_packet = self._create_packet()
            return True
        return False

    def _create_packet(self):
        length = random.randint(5, 20)
        packet = [' ']*length
        for i in range(length):
            packet[i] = chr(random.randint(ord('A'), ord('z')))
        return ''.join(packet)

    def get_packet(self):
        return self._current_packet

    def delete_packet(self):
        self._current_packet = None


class InternetProcess:
    def __init__(self):
        self._new_packets = False
        self._Alice = None

    def check_for_packet(self):
        if self._Alice.get_packet() is not None:
            return True
        return False

    def read_packet(self):
        if self._new_packets:
            return self._Alice.get_packet()
        return None

    def delete_packet(self):
        self._Alice.delete_packet()

    def assign_alice(self, alice):
        self._Alice = alice


class BobApplication:
    def check_for_packet(self, other):
        if other.check_for_packet():
            return True
        return False

    def delete_packet(self, other):
        other.delete_packet()


Alice = AliceApplication()
internet = InternetProcess()
internet.assign_alice(Alice)
Bob = BobApplication()

for i in range(30):
    print(f'Time is: {i}')
    if Alice.act():
        print("Created the packet", Alice.get_packet())
    if Bob.check_for_packet(internet):
        print('Bob detected the packet')
        Bob.delete_packet(internet)


















