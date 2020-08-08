from GameFrame import RoomObject


class Goal(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('dirt.png')
        self.set_image(image, 32, 32)

        self.register_collision_object('Player')

    def handle_collision(self, other, other_type):
        self.room.running = False
