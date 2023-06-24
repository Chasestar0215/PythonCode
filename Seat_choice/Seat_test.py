import tkinter as tk

seat_info = get_seat_info()

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

for row in seat_info:
    for seat in row():
        if seat.is_selected():
            canvas.create_rectangle(
                seat.x, seat.y, seat.x + seat.width, seat.y + seat.height,
                fill='red', outline='black'
            )
        else:
            canvas.create_rectangle(
                seat.x, seat.y, seat.x + seat.width, seat.y + seat.height,
                fill='white', outline='black'
            )


def on_click(event):
    x, y = event.x, event.y

    seat = get_seat_at(x, y)
    if not seat.is_selected():
        reverse_seat(seat)

        canvas.create_rectangle(
            seat.x, seat.y, seat.x + seat.width, seat.y + seat.height,
            fill='red', outline='black'
        )


canvas.bind('<Button-1>', on_click)

root.mainloop()
