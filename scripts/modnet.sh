#!/bin/sh

#ICS="$HOME/public_html/misc/modnet.ics"
ICS=$1
OLD="$ICS.old"
MODNET="./scripts/modnetcal"
/bin/cp $ICS $OLD
$MODNET --ical < $OLD > $ICS || /bin/cp $OLD $ICS


