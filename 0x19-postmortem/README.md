![This is an image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/265/uWLzjc8.jpg)

# Issue summary

Access to the server endpoint using curl 0:80 was returning `curl: (7) Failed to connect to 0 port 80: Connection refused`. The issue lasted for 5 hours after the last server update from a team member up to when it was resolved. The Airbnb clone website was inaccessible to half of the clients during the 5 hours of downtime. This was caused by a wrong port value set in the Nginx configuration files.

# Duration (East Africa Time).

Monday, 27 October 2022

10:00 AM: Logged into the server and the Nginx server was not responding to requests on socket 0:80

10:05: Begun web debugging to locate issues. This involved the steps;

Check if Nginx is running

`sudo service nginx status`

Showed Nginx is not running

Check if there are nginx processes running.

`pgrep -lf nginx`

Showed the program is active and running.

Tried to restart Nginx

`sudo service nginx restart`

failed


Check log files

`cat /var/log/nginx/error.log | tail -10`
bind() to [::]:8080 failed (98: Address already in use)

Check processes using ports

`netstat -lpn`
Nginx was listening on port 8080

Checked Nginx configuration files;

`cat /etc/nginx/sites-available/default`

`cat /etc/nginx/sites-enabled/default`

The problem was with the Nginx configuration in the file `/etc/nginx/sites-enabled/default`.

Nginx was listening on `8080` instead of `80`.

10:31: Nginx was configured to listen on port 80 and restarted successfully.

# Root Cause.

![This is an image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif)

Nginx was listening to port 8080 instead of port 80 used to access the web server endpoint. The Nginx server config file `/etc/nginx/sites-enabled/default` was set to listen to port `8080` instead of port `80`. The issue was fixed by changing the default port 8080 to 80 using a shell command:

`sudo sed -i 's/8080 default_server/80 default_server/g' /etc/nginx/sites-enabled/default`

Nginx was restarted by the command:

`sudo service nginx restart`

# Corrective and Preventative measures.
Nginx server management can be improved by using script automation. A server monitoring tool should be set up to enable quick response to problems.

## What to do
* Restrict users' access to the server to avoid unconfirmed server changes.
* Create Nginx automation script in shell or puppet.
* Install a server monitoring system and a response team to handle server problems
