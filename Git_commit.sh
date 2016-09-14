#!/bin/sh

#echo -n "${GREEN}${NC}"
#cd /media/HDD/0_Programmierung/bin/Magic_Shapes/
#cd /media/HDD/0_Programmierung/bin/Snake_Game/

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "${GREEN}Available Repositorys:${NC}"
echo "${GREEN}[1.]Magic_Shapes${NC}"
echo "${GREEN}[2.]Snake_Game${NC}"
echo "${GREEN}Select Repository:${NC}"
read repo
case $repo in
    1) cd /media/HDD/0_Programmierung/bin/Magic_Shapes/ ;;
    2) cd /media/HDD/0_Programmierung/bin/Snake_Game/ ;;
    *) echo -n "${RED}No such Repository!${NC}" && sleep 5 && exit;;
esac
    

echo -n "${GREEN}Files to Stage:${NC}"
echo ""
git status
echo -n "${GREEN}When you want to stange the files press any key, else press Ctrl+C${NC}"
read itisnotimportant
echo -n "${GREEN}Staged Files:${NC}"
echo ""
git add --all
git status
echo -n "${GREEN}When you want to commit these files press any key, ele press Ctrl+C${NC}"
read itisnotimportant
echo -n "${GREEN}Git message for Magic_Shapes commit: ${NC}"
read theanswer
echo -n "${GREEN}committing Magic_Shapes with message: ${RED}$theanswer ${NC}"
echo ""
git commit -a -m "$theanswer"
echo -n "${GREEN}Succesfully committed"
echo ""
echo -n "${GREEN}Do you want to push them to their origin? [else press Ctrl+C]${NC}"
read pushit
echo -n "${GREEN}Pushing to origin...${NC}"
echo ""
git push 
echo -n "${GREEN}Pushed succesfully to origin!${NC}"
echo ""
