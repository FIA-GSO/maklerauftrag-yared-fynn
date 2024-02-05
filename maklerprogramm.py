room_dictionary = {
 "Id": [],
 "Name": [],
 "Area": []
}

has_another_room = True
counter = 1

while (has_another_room == True):
 room_dictionary["Id"].append(counter)
 print("Bitte gib den Raumbezeichnung an")
 room_name = input()
 has_another_area = True
 room_area = 0
 while (has_another_area == True):
  room_dictionary["Name"].append(room_name)
  print("Bitte gib die Länge an")
  room_length = int(input())
  print("Bitte gib die Breite an")
  room_width = int(input())
  room_area += room_width * room_length
  print("Gibt es noch eine weiter Fläche [Y/N]")
  if (input() == "N"):
    has_another_area = False
    room_dictionary["Area"].append(room_area)


 room_dictionary["Area"].append(room_area)
 # Gesamtfläche
 # Raumbezeichnungen eingeben
 # Unberechnete Räume vorhanden ?
 # Wenn wahr gebe Seitenlänge ein
 # Noch eine Fläche ?
 # Wenn ja
 # Wenn nein Ende
 # Addiere auf Gesamtfläche
 # Noch ein Raum ?
 # Wenn ja Zeile 7
# Wenn nein Ende
# Ausgabe der Raumflächen mit Raumbezeichnungen
# Ausgabe der Gesamtfläche