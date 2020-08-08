from GameFrame import Level, Globals
from Objects import Player, Block, Goal, Dirt


class CourtYard(Level):

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.background_colour = (51, 43, 0)

        self.room_items = []

        # - Set up maze, objects 32x32 - #
        room_objects = [
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
            'DBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBD',
            'DB                                              BD',
            'DB                                              BD',
            'DB                                              BD',
            'DB                                              BD',
            'DB                        B                     BD',
            'DB       B  BBBBBBBB      B                     BD',
            'DB       B         B      B                     BD',
            'DB       B         B      B                     BD',
            'DB       B         B      B                     BD',
            'DB       BBBBBBB   B      B                     BD',
            'DB                                              BD',
            'DB                                              BD',
            'DB           BBBBBB  BBBBBBB                    BD',
            'DB           B             B                    BD',
            'DB           B       P     B                    BD',
            'DB           B             B                    BD',
            'DB           B             B                    BD',
            'DB           BBBBBBBBBBBB  B                    BD',
            'DB                             BBBBB   BBBBBB   BD',
            'DB                                              BD',
            'DB       BB   BBBBBBBBBBB                       BD',
            'DB       B              B   BBBBBBBBBBBBBBBBB   BD',
            'DB       B              B   B                   BD',
            'DB       B    BBBBBBB   B                       BD',
            'DB       B   BBBBB     BBBBBBBBBBBBBBBBBBBBB    BD',
            'DB       B   B                             B    BD',
            'DB       B   B                             B    BD',
            'DBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB  BBBBBBD',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDGGDDDDDDD'
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == 'B':
                    new_block = Block(self, j*32 - 200, i*32 - 200)
                    self.add_room_object(new_block)
                    self.room_items.append(new_block)
                elif obj == 'P':
                    self.add_room_object(Player(self, j*32 - 200, i*32 - 200))
                elif obj == 'G':
                    new_goal = Goal(self, j*32 - 200, i*32 - 200)
                    self.add_room_object(new_goal)
                    self.room_items.append(new_goal)
                elif obj == 'D':
                    new_dirt = Dirt(self, j*32 - 200, i*32 - 200)
                    self.add_room_object(new_dirt)
                    self.room_items.append(new_dirt)

    def shift_room_left(self):
        for item in self.room_items:
            item.x -= Globals.move_speed

    def shift_room_right(self):
        for item in self.room_items:
            item.x += Globals.move_speed

    def shift_room_up(self):
        for item in self.room_items:
            item.y -= Globals.move_speed

    def shift_room_down(self):
        for item in self.room_items:
            item.y += Globals.move_speed
