#! /bin/bash

echo "enter your name:"
read name
if [[ -z $name ]]
then
	echo "bye"
	exit 0
fi

echo "enter your age:"
read age

while [[ $age -ne 0 ]]

do
	if [[  $age -le 16 ]]
	then
		group="child"
	elif [[ $age -le 25 ]]
	then
		group="youth"
	else
		group="adult"
	fi
	
	echo "$name, your group is $group"
	
	echo "enter your name:"
	read name
	
	if [[ -z $name ]]
	then
		break
	fi

	echo "enter your age:"
	read age
done

echo "bye"
exit 0
