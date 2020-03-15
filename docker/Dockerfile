FROM ubuntu:18.04
RUN apt-get update && apt-get -y upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install apt-utils php7.2 php7.2-cli php7.2-common libapache2-mod-php apache2 unzip
RUN apt-get install php7.2-curl php7.2-gd php7.2-json php7.2-mbstring php7.2-intl php7.2-mysql php7.2-xml php7.2-zip -y
WORKDIR /var/www/html
RUN rm index.html
ADD https://github.com/EzioAARM/wordpress-cicd/archive/develop.zip ./code.zip
RUN unzip code.zip && mv /var/www/html/wordpress-cicd-develop/* /var/www/html
ADD https://wordpress-cicd.s3.amazonaws.com/wp-config.php ./wp-config.php
RUN chmod +777 wp-config.php
CMD apachectl -DFOREGROUND