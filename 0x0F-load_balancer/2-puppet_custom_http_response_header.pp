# Add custom HTTP Header with Puppet
exec { 'HTTP_header':
  command  => 'sudo apt-get -y update;
	       sudo apt-get -y install nginx;
	       echo "Hello World" | sudo tee /var/www/html/index.html;
	       sudo chmod 777 /etc/nginx;
	       sudo chmod 777 /etc/nginx/nginx.conf;
	       sudo sed -i "/sendfile on;/ a add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf;
               service nginx start',
  provider => 'shell',
}
