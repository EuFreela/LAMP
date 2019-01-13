#!/bin/bash

# UPDATE
if ! apt-get update
then
    	echo "Não foi possível atualizar os repositórios. Verifique seu arquivo /etc/apt/sources.list"
    	exit 1
fi
echo "Atualização feita com sucesso"
echo "Atualizando pacotes já instalados"

if ! apt-get dist-upgrade -y
then
    	echo "Não foi possível atualizar pacotes."
    	exit 1
fi
echo "Atualização de pacotes feita com sucesso"


# LAMP
echo "Instalação do APACHE2"
if ! apt install apache2 -y
then
	echo "Não foi possível instalar o apache2"
	exit 1
fi
echo "Instalado apache2. http://localhost"

#LAMP - MYSQL
echo "Instalação do MYSQL"
if ! apt install mysql-server -y
then
	echo "Não foi possível instalar o mysql"
fi
echo "Instalado o mysql"

#echo "Configuração Mysql"
mysql_secure_installation
#echo "Use: SELECT user,authentication_string,plugin,host FROM mysql.user;"
#echo "Use: ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '##ChinaTown##';"
#echo "Use: FLUSH PRIVILEGES;"
#echo "Use: exit "
#mysql

#LAMP - PHP
echo "Instalação do PHP"
if ! apt install php libapache2-mod-php php-mysql -y && apt install php-cli -y
then
	echo "Não foi possível instalar o php"
	exit 1
fi
echo "Instalado o PHP"

#lamp - phpmyadmin
echo "Instalação do PHPMYADMIN"
if ! apt-get install phpmyadmin php-mbstring php-gettext -y && phpenmod mcrypt && phpenmod mbstring
then
	echo "Não foi possivel instalar o phpmyadmin"
	exit 1
fi
echo "Instalado o PHPMYADMIN"

echo "Instalar o NODEJS"
if ! apt-get install nodejs -y && apt-get install build-essential -y
then
	echo "Não foi possível instalar o nodejs"
	exit 1
fi
echo "Instalado o nodejs"

echo "Instalar o NPM"
if ! apt-get install npm -y
then
	echo "Não foi possível instalar o npm"
	exit 1
fi
echo "Instalado o npm"

echo "Instalar o workbanch"
if ! apt install mysql-workbench -y
then
	echo "Não foi possível instalar o workbench"
	exit 1
fi
echo "Instalado o workbench"

echo "VS CODE"
if ! apt-get install snapd snapd-xdg-open -y
then
	echo "Não foi possivel instalar dependencias VSCODE"
	exit 1
fi

# VSCODE
if ! snap install --classic vscode
then
	echo "Não foi possivel instalar vscode"
	exit 1
fi
snap refresh vscode
#snap remove vscode

#GIT
#echo "Instalando git"
#if ! apt install git -y
#then
#	echo "Não fi posível instalar github"
#	exit 1
#fi
#echo "Instalado git"

#COMPOSER
echo "Instalando o composer"
EXPECTED_SIGNATURE=$(wget -q -O - https://composer.github.io/installer.sig)
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" 
ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-setup.php');") 

if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ] 
then 
    >&2 echo 'ERROR: Invalid installer signature' 
    rm composer-setup.php 
    exit 1 
fi 

php composer-setup.php --quiet 
RESULT=$? 
rm composer-setup.php
echo "Foi instalado o composer"

#echo "Heroku"
#if ! snap install heroku --classic -y
#then
#	echo "Não foi possível instalar heroku"
#	exit 1
#fi
#echo "Instalado heroku"


#echo "Instalando o Java"
#if ! apt-get install default-jre -y && apt-get install default-jdk -y
#then
#	echo "Não foi possível instalar o JRE"
#	exit 1
#fi
#echo "Instalado o JRE"

#echo "Instalando Razor"
#wget -c http://downloads.razorsql.com/downloads/7_0_8/razorsql7_0_8_linux_x86.zip
#unzip razorsql7_0_8_linux_x86.zip




echo "Restartando os serviços.."
systemctl restart apache2
echo "Criando teste PHP.."
echo "<?php phpinfo ?>" > /var/www/html/info.php
echo "Teste php: http://localhost/info.php"
echo "Teste phpmyadmin: http://localhost/phpmyadmin"

#echo "node versão"
#node -v
#echo "npm versão"
#npm -v
#echo "Para abrir o Razor SQL: cd razorsql; sh razorsql.sh"




