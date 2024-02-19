room_dictionary = {
    "Id": [],
    "Name": [],
    "Area": []
}

has_another_room = True
counter = 1

while has_another_room:
    room_dictionary["Id"].append(counter)
    room_name = input("Bitte gib den Raumbezeichnung an")
    room_dictionary["Name"].append(room_name)
    has_another_area = True
    room_area = 0
    while has_another_area:
        room_length = int(input("Bitte gib die Länge an"))
        room_width = int(input("Bitte gib die Breite an"))
        room_area += room_width * room_length
        next_area = input("Gibt es noch ein weiteres Rechteck? [Y/N]").strip()
        while next_area != "N" and next_area != "n" and next_area != "Y" and next_area != "y":
            print("Falsche Eingabe -> [Y/N]")
            next_area = input().strip()
        if next_area == "N" or next_area == "n":
            has_another_area = False
            room_dictionary["Area"].append(room_area)
            break
        elif next_area == "Y" or next_area == "y":
            continue
    room_dictionary["Area"].append(room_area)
    next_room = input("Gibt es noch einen weiteren Raum? [Y/N]")
    while next_room != "N" and next_room != "n" and next_room != "Y" and next_room != "y":
        print("Falsche Eingabe -> [Y/N]")
    if next_room == "N" or next_room == "n":
        has_another_room = False
        print(room_dictionary["id"][1])
        print("Gesamtflaeche: ")
        break
    elif next_room == "Y" or next_room == "y":
        continue
