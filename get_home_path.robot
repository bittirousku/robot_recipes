*** Settings ***
Library		Selenium2Library
Library		./utils.py


*** Test cases ***
Test home dir getting
	Get home dir


*** Keywords ***
Get home dir
	${home_dir}=	Run keyword if	os.sep == "/"	get linux home dir
	...				ELSE			construct win home dir
	should be true		"${home_dir}" == "/home/robot/"

Get linux home dir
	${linux_dir}=		Get Environment Variable		HOME	NA
	[Return]			${linux_dir}

Construct win home dir
	${win_dir}=		set variable	C:\\Users\\robot
	[Return]		${win_dir}


# run keyword if näköjään palauttaa aina Nonen jos ehto ei täyty
