#!/bin/sh


key="AADF11C13DD39517B94BEFEF158637EE4061D47DE1BD105B507520B441867EE2"
iv="7E4461B4C7A3062543E10E979F8057AF"
#iv="0000000000000000000000000000000"

function encrypt(){
	echo "------"
	echo $1
	for file in $(ls $1);  
	do  
			if [ -d $1"/"$file ]  
			then  
					encrypt $1"/"$file  
			else  
					echo "$file" |grep -q ".json"
					if [ $? -eq 0 ]
					then
						echo "encrypt -- "
						echo $1"/"$file
						name=$(md5 -s $file)
						echo "name -"$name
						finalname=${name#*= }
						#finalname=${finalname:1:32}
						echo "finalname - "$finalname
						openssl aes-256-cbc -e -in $1"/"$file -out $1"/"$finalname".unity3d" -K ${key} -iv ${iv} #-p
					fi
			fi  
	done
}


function decrypt(){
	echo "------"
	echo $1
	for file in $(ls $1);  
	do  
			if [ -d $1"/"$file ]  
			then  
					decrypt $1"/"$file  
			else  
					echo "$file" |grep -q ".unity3d"
					if [ $? -eq 0 ]
					then
						echo "encrypt -- "
						echo $1"/"$file
						openssl aes-256-cbc -d -in $1"/"$file -out $1"/"$file"_bak" -K ${key} -iv ${iv} #-p
					fi
			fi  
	done
}

encrypt $(pwd)/res/data
#decrypt $(pwd)/res/data
