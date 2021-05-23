class Room:
    def __init__(self, name, capacity, till, entry_fee):
        self.name = name
        self.capacity = capacity
        self.till = till
        self.entry_fee = entry_fee
        self.occupants = []
        self.song_list = []

    def occupants_queue_length(self):
        return len(self.occupants)

    def add_guest_to_room(self, guest):
        if self.occupants_queue_length() == self.capacity:
            return
        self.occupants.append(guest)

    def remove_guest_from_room(self, guest):
        if self.occupants_queue_length() == 0:
            return
        self.occupants.remove(guest)

    def song_list_length(self):
        return len(self.song_list)

    def add_song_to_room(self, song):
        self.song_list.append(song)

    def increase_till_money(self, amount):
        self.till += amount

    def take_entry_from_guest_and_add_to_till(self, room, guest):
        guest.reduce_money(room.entry_fee)
        self.increase_till_money(room.entry_fee)

    # def take_entry_fee_from_guest(self):
    #     guest.reduce_money(room.entry_fee)

    # def is_room_at_capacity(self):
    #     if self.occupants_queue_length() == self.capacity:
    #         return True

    #     return False