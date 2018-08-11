#!/bin/sh

# Télécharge la liste et l'imprime au format :
# Date ISO\tNom\tCapacité\tPlaces occupées\tPlaces Restantes
# un - est affiché si la piscine est fermée (ou vide?)

curl -s http://www.piscines-patinoires.lyon.fr | \
    pup 'section.white-area td text{}'| \
    awk '/[A-Za-z]/ {printf "\n%s",$0} /^[0-9-]+$/ {printf "\t%s", $0}'| \
    grep -v '^$'| \
    while read i;do echo -e "$(date -Iseconds)\t$i";done