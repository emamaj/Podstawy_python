#zmienne w pamięci operacyjnej

pierwszaCzescImienia = "Ale"
drugaCzescImienia = "ksander"
caleImie = pierwszaCzescImienia + drugaCzescImienia
print("id=", id(pierwszaCzescImienia))

print("cale imie = " + caleImie)

pierwszaCzescImienia += drugaCzescImienia

print("id=", id(pierwszaCzescImienia))

print("cale imie = " + pierwszaCzescImienia)