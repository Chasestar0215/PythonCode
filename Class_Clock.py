class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.id = 8848
clock1.price = 19.9
print(f'闹钟编号为:{clock1.id},价格是:{clock1.price}')
clock1.ring()
