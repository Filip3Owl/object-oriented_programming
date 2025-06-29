class Body:
    pass

Body.high = 1.8
Body.weight = 80

print(f'High: {Body.high}, Weight: {Body.weight}') # High: 1.8, Weight: 80


class High:
    hight = 1.8

object_high = High()
print(f'High: {object_high.hight}')  # High: 1.8

object_high_2 = High()
object_high_2.hight = 1.9
print(f'High: {object_high_2.hight}')  # High: 1