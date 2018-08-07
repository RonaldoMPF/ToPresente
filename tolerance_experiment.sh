#!/bin/bash

for value in {60..1}
do
    echo $'tolerance: '$value >> ./result.txt
    face_recognition ./data/sample/ ./data/test/ > ./result.txt
done

echo All done
