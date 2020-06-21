#! /bin/bash

read arg1 operation arg2

while [[ ($arg1 -ne "exit") && (-n $arg2) ]]
do
	case $operation in
	"+") let "ans = $arg1 + $arg2";;
	"-") let "ans = $arg1 - $arg2";;
	"*") let "ans = $arg1 * $arg2";;
	"/") let "ans = $arg1 / $arg2";;
	"%") let "ans = $arg1 % $arg2";;
	"**") let "ans = $arg1 ** $arg2";;
	*) echo "error"; exit 0
	esac
	echo "$ans"
	read arg1 operation arg2
done
case $arg1 in
"exit") echo "bye";;
*) echo "error";;
esac
exit 0
