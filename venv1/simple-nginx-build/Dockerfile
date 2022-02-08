FROM ubuntu

# Install Nginx
RUN apt-get update 
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install nano
RUN rm -rf /var/lib/apt/lists/*
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx

# Define mountable directories.
VOLUME  ["/etc/nginx/sites-enabled","/etc/nginx/certs","/etc/nginx/conf.d"]

# Deine owrking directory.
WORKDIR /etc/nginx

# Define default command.
CMD ["nginx"]