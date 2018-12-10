#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then echo -e 'This script must be run as root' ; exit 1 ; fi

echo "deb http://mirror.jaleco.com/mariadb/repo/10.3/debian `lsb_release -cs` main" > /etc/apt/sources.list.d/mariadb.list
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C74CD1D8 #MariaDB

debconf-set-selections <<< "mysql-server mysql-server/root_password password `cat /tmp/ecp_dbpass`"
debconf-set-selections <<< "mysql-server mysql-server/root_password_again password `cat /tmp/ecp_dbpass`"

apt update ; apt -y install mariadb-server mariadb-client

#-----------------------------------------------------------------------------------------
# 02 - Configuring MySQL
#-----------------------------------------------------------------------------------------
sed -i "s/skip-external-locking//" /etc/mysql/my.cnf
mysql -uroot -p"`cat /tmp/ecp_dbpass`" -e "UPDATE mysql.user SET plugin='' WHERE User='root';"
crudini --set /etc/mysql/conf.d/mariadb.cnf 'mysqld' 'bind-address' `cat /tmp/db_bindaddr`
crudini --set /etc/mysql/conf.d/mysql.cnf 'mysql' 'host'     `cat /tmp/db_bindaddr`
crudini --set /etc/mysql/conf.d/mysql.cnf 'mysql' 'password' `cat /tmp/ecp_dbpass`
crudini --set /etc/mysql/conf.d/mysql.cnf 'mysql' 'user'     'root'

crudini --set /etc/mysql/conf.d/mysql.cnf 'mysqldump' 'host'     `cat /tmp/db_bindaddr`
crudini --set /etc/mysql/conf.d/mysql.cnf 'mysqldump' 'password' `cat /tmp/ecp_dbpass`
crudini --set /etc/mysql/conf.d/mysql.cnf 'mysqldump' 'user'     'root'

