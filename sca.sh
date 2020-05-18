#!/bin/bash

RED=$(tput setaf 1) 
GREEN=$(tput setaf 2) 
WHITE=$(tput setaf 7) 
BLUE=$(tput setaf 4) 

begin=$(date +"%s")
echo "${GREEN}[gelbooru/safebooru stealer] / [-sin]"

echo "tags/allias:"
read -r kode
echo "count:"
read -r count
echo -e "reading /${GREEN}$kode ..Continue? (Y/N): "
echo -e "reading source for /${GREEN}$kode ..
${WHITE}"
var="${kode}"
json="cat ${kode}.html"
echo ${GREEN}$var

mkdir -pv "bash~${var}" 
#do

cd "bash~${var}";

#cf issues
wget --page-requisites --span-hosts -O ${kode}.html "https://safebooru.org/index.php?page=dapi&s=post&q=index&limit=${count}&tags=${kode}"; 

${json} | grep -o 'file_url="[^"]*' | sed 's/file_url="//g' > links.txt; 
wget -i links.txt # -i $argv = process


#length
termin=$(date +"%s")
difftimelps=$(($termin-$begin))
echo "${WHITE}$(($difftimelps / 60)) minutes and $(($difftimelps % 60)) sec. elapsed ${RED}booruscraper"
