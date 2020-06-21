#! /bin/bash

gcd () 
{
	let "r2 = $2 % $1"
	if [[ r2 -eq 0 ]]
	then
		echo "GCD is $1"
	else
		gcd $r2 $1
	fi
}

read M N

while [[ -n $M ]]
do
	if [[ $M -eq $N ]]
	then
		echo "GCD is $M"
	elif [[ $M -gt $N ]]
	then
		let "r=M-N"
		gcd $r $N
	else
		let "r=N-M"
		gcd $M $r
	fi
	read M N
done
echo "bye"
exit 0
