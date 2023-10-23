#!/bin/dash
#bash/sh

# Installation of the environment for the application

NAME_ENVIRONMENT="projenv"
VERSION_PYTHON="3.9.13"

environments=`conda env list | grep $NAME_ENVIRONMENT`
#echo $environments

echo ">To validate whether the environment exists"
if [ -z "$environments" ]
then
    echo ">>>The environment $NAME_ENVIRONMENT does NOT exist. Thus we proceed to create it."

    echo "\n\n\n>>> ##### It is expected to press ENTER. Press ENTER and wait for the result. The content might be cleaned and cursor may be on the top of the screen"

    result=`conda create --name $NAME_ENVIRONMENT python=$VERSION_PYTHON`

else
    echo ">>>The environment $NAME_ENVIRONMENT does exist"
fi


echo ">Retrieving conda environments to check if current projenv does exist or not"
environments=`conda env list | grep $NAME_ENVIRONMENT`
if [ -z "$environments" ]
then
    echo "The environment does not exist and was not created"
    exit 1
fi


#path_source=$(echo `conda info | grep -i 'base environment'` | awk '{for (i=1; i<=NF; i++) if ($i ~ /^\/.*/) print $i}')
#echo $path_source

#echo ". $path_source/etc/profile.d/conda.sh"
#result=`. $path_source/etc/profile.d/conda.sh`
#echo $?

eval "$(conda shell.bash hook)"

conda activate $NAME_ENVIRONMENT

active_environment=$(echo `conda info | grep -i 'active environment'` | grep $NAME_ENVIRONMENT)
if [ -z "$active_environment" ]
then
    echo ">>>Environment $NAME_ENVIRONMENT was NOT activated"
    exit 1
else
    echo ">>>Environment $NAME_ENVIRONMENT was NOT activated successfully :)"
fi

echo "To install pip requirements"
pip install -r requirements.txt
echo $?

echo "To install npm dependencies"
echo $?

