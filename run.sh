#!/bin/bash
# J. Dvd Zl
echo "Running"
echo "Add all files"
git add .
git commit -m $1
#git remote set-url  origin https://github.com/unionsoftware/Simulation
git remote set-url  origin  git+ssh://git@github.com/unionsoftware/Simulation

git push -f origin master 

echo "Finished."
