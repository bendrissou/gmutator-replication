# Delete certain whitespaces in xml input.
# Pugixml program doen not accept whitespace in certain locations.

XML_FILE=$1
sed -i 's/< /</g' ${XML_FILE}
sed -i 's/<? xml/<?xml/g' ${XML_FILE}
sed -i 's/< \/ /<\//g' ${XML_FILE}
sed -i 's/<\/ /<\//g' ${XML_FILE}
