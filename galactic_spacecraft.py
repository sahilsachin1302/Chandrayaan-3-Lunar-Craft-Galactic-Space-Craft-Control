class GalacticSpaceCraft:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.direction = 'N'

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'Up':
            self.z += 1
        elif self.direction == 'Down':
            self.z -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'Up':
            self.z -= 1
        elif self.direction == 'Down':
            self.z += 1

    def turn_left(self):
        self.direction = {
            'N': 'W',
            'S': 'E',
            'E': 'N',
            'W': 'S',
            'Up': 'N',
            'Down': 'S',
        }[self.direction]

    def turn_right(self):
        self.direction = {
            'N': 'E',
            'S': 'W',
            'E': 'S',
            'W': 'N',
            'Up': 'N',
            'Down': 'S',
        }[self.direction]

    def turn_up(self):
        if self.direction != 'Up':
            self.direction = 'Up'

    def turn_down(self):
        if self.direction != 'Down':
            self.direction = 'Down'

    def execute_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
            elif command == 'u':
                self.turn_up()
            elif command == 'd':
                self.turn_down()

        return (self.x, self.y, self.z), self.direction
