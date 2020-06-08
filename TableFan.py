class Fan(object):
    def __init__(self, manufacturer='Binatone', cost=0, speed=0, height=5, blades=2, color='black', is_on=False,
                 is_new=False, side_movement=False, degree=90):
        self.manufacturer = manufacturer
        self.price = cost
        self.height = height
        self.number_of_blades = blades
        self.color = color
        self.state = is_on
        self.speed = speed
        self.is_new = is_new
        self.side_to_side_movement = side_movement
        # if self.side_to_side_movement:
        self.degree = degree
        # else:
        #     self.degree = 0

    def get_price(self):
        """Return price of fan"""
        return self.price

    def change_price(self, price=0):
        """Set price of fan"""
        self.price = price

    def set_state(self, is_on=False):
        """Turn fan on or off. If on, fan speed is set at 1 by default"""
        self.state = is_on
        if is_on:
            self.increase_speed_by()
            print("Fan is on")
        else:
            print("Turn fan on")

    def get_state(self):
        """Returns state of the fan. On/Off"""
        return self.state

    def increase_speed_by(self, value=1):
        """Increase fan speed if fan is on. Fan speed cannot exceed 5"""
        if self.get_state():  # if fan is on
            if value + self.speed <= 5:  # speed can only be increased by values 1 - 4
                self.speed += value
                return self.speed
            else:
                print("Max speed is 5.\nCurrent speed is: {}".format(self.speed))
                return self.speed
        else:
            print("Turn fan on to increase speed.")

    def decrease_speed_by(self, value=1):
        """Decrease fan speed if fan is on. Fan speed cannot be below 1"""
        if self.get_state():
            if self.speed - value >= 1:  # lowest speed is 1
                self.speed -= value
                return self.speed
            else:
                print("Current speed is: {}. Fan cannot go below 1".format(self.speed))
                return self.speed
        else:
            print("Turn fan on to decrease speed")

    def can_move_sideways(self, side_movement=False):
        """Enable and disable side movements"""
        if self.get_state():
            self.side_to_side_movement = side_movement
            if self.side_to_side_movement:
                print("Fan moving side ways in {} degree...".format(self.degree))
            else:
                print("Enable side to side movement")
        else:
            print("Turn fan on to enable side movement")

    def __str__(self):
        return "A {} {} blade {} fan. Price: ${}".format(self.color, self.number_of_blades, self.manufacturer,
                                                         self.price)


def main():
    fan = Fan('Hisense', 1500, blades=3, color='white', is_on=False, is_new=True, side_movement=False, degree=45)
    print("New fan" if fan.is_new else "Old fan")  # Ternary operation
    fan.set_state(True)
    print("Speed: {}".format(fan.increase_speed_by(3)))
    print("Speed: {}".format(fan.decrease_speed_by(2)))
    fan.can_move_sideways(True)
    print(fan)
    print('\n')
    fan2 = Fan(cost=2000)
    print(fan2)


main()
