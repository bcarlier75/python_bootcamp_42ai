MY_PATH=$(which python)
GOOD_PATH='/sgoinfre/goinfre/Perso/bcarlier/anaconda3/bin/python'
if [ "$MY_PATH" == "$GOOD_PATH" ]; then
	echo 'Python is already installed, do you want to reinstall it ?'
	read -p '[yes|no]' answer
	if [ "$answer" == "yes" ]; then
		#rm -rf /sgoinfre/goinfre/Perso/bcarlier/anaconda3
		echo 'Python has been removed.'
		#cd /sgoinfre/goinfre/Perso/bcarlier/
		#curl -Ok https://repo.continuum.io/archive/Anaconda3-2019.10-MacOSX-x86_64.sh
		#bash Anaconda3-2019.10-MacOSX-x86_64.sh -p anaconda3
		#rm Anaconda3-2019.10-MacOSX-x86_64.sh
		#export PATH="/sgoinfre/goinfre/Perso/bcarlier/anaconda3/bin:$PATH"
		echo 'Python has been installed.'
	else
		echo 'exit.'
	fi
else
		#cd /sgoinfre/goinfre/Perso/bcarlier/
		#curl -Ok https://repo.continuum.io/archive/Anaconda3-2019.10-MacOSX-x86_64.sh
		#bash Anaconda3-2019.10-MacOSX-x86_64.sh -p anaconda3
		#rm Anaconda3-2019.10-MacOSX-x86_64.sh
		#export PATH="/sgoinfre/goinfre/Perso/bcarlier/anaconda3/bin:$PATH"
		echo 'Python has been installed.'
fi
