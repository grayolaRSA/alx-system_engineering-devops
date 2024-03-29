# automates all the bash scripts in puppet file
# installs nginx server | adds 300 and 400 error codes

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\\/redirect_me return 301 https:\/\/www.freecodecamp.org\/ permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
