# Created by Fynn and Yared

# Initialiserung des Dictonarys
room_dictionary = {
    "Id": [],
    "Name": [],
    "Area": []
}
# Initialiesierung der Variable für eine fußgesteuerte Schleife
has_another_room = True
counter = 1
# Schleife, die sich so lange wiederholt, bis der Benutzer sagt, dass es keinen weiteren Raum gibt
while has_another_room:
    # Der Raumname und die RaumId werden im Dictonary gespeichert.
    room_dictionary["Id"].append(counter)
    room_name = input("Bitte gib die Raumbezeichnung an: ")
    room_dictionary["Name"].append(room_name)
    # Variable für eine fußgesteuerte Schleife
    has_another_area = True
    room_area = 0
    # Schleife, die sich so lange wiederholt, bis der Benutzer sagt, dass es kein weiteres Rechteck gibt
    while has_another_area:
        # Der Benutzer gibt Länge und Breite des aktuellen Rechtecks ein
        room_length = int(input("Bitte gib die Länge an: "))
        room_width = int(input("Bitte gib die Breite an: "))
        # Gesamtfläche wird aus Länge und Breite berechnet und der Raumfläche hinzugefügt
        room_area += room_width * room_length
        # Der Benutzer wird nach einem weiteren Rechteck gefragt
        next_area = input("Gibt es noch ein weiteres Rechteck? [Y/N]").strip()
        while next_area != "N" and next_area != "n" and next_area != "Y" and next_area != "y":
            # Wenn die Eingabe nicht Y,y,n oder N ist, wird der Benutzer nach einer neuen Eingabe gefragt
            print("Falsche Eingabe -> [Y/N]")
            next_area = input().strip()
        if next_area == "N" or next_area == "n":
            # Wenn es keinen weiteren Raum gibt, wird die while has_another_area Schleife verlassen
            has_another_area = False
            break
        elif next_area == "Y" or next_area == "y":
            # Wenn es einen weiteren Raum gibt, geht es wieder zum Anfang der Schleife
            continue
    # Die Raumfläche wird dem Dictonary hinzugefügt
    room_dictionary["Area"].append(room_area)
    counter += 1
    # Der Benutzer wird gefragt, ob es noch einen weiteren Raum gibt
    next_room = input("Gibt es noch einen weiteren Raum? [Y/N]")
    while next_room != "N" and next_room != "n" and next_room != "Y" and next_room != "y":
        # Der Input wird validiert, wenn der Input invalid ist, wird nach einem neuen Input gefragt
        print("Falsche Eingabe -> [Y/N]")
        next_area = input().strip()
    if next_room == "N" or next_room == "n":
        # Wenn es keinen weiteren Raum gibt, werden alle Räume ausgegeben und die Schleife beendet
        has_another_room = False
        ids = room_dictionary["Id"]
        names = room_dictionary["Name"]
        areas = room_dictionary["Area"]
        gesamtflaeche = 0
        print("\n------------------------------------------------\n")
        print(f"{"Raumnummer":18}|{"Raumbezeichnung":18}|{"Fläche":18}")
        print("--------------------------------------------")
        for i in range(len(ids)):
            # Zur Gesamtfläche werden alle Raumflächen addiert.
            gesamtflaeche += areas[i]
            # Jeder einzelner Raum wird ausgegeben
            print(f"{str(ids[i]):18}|{names[i]:18}|{str(areas[i]):18}")
        print("------------------------------------------------")
        print("Gesamtflaeche: " + str(gesamtflaeche))
        break
    elif next_room == "Y" or next_room == "y":
        # Es gibt noch einen weiteren Raum und die Schleife wird noch einmal wiederholt für den nächsten raum
        continue
