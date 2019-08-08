# 0x0C. Web server

## Learning Objectives
* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests
* DNS
* What DNS stands for
* What is DNS main role
* DNS Record Types
* A
* CNAME
* TXT
* MX

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

---

### [0. Transfer a file to your server](./0-transfer_file)
Write a Bash script that transfers a file from our client to a server:

Requirements:

* Accepts 4 parameters
1. The path to the file to be transferred
1. The IP of the server we want to transfer the file to
1. The username scp connects with
1. The path to the SSH private key that scp uses
* Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
* scp must transfer the file to the user home directory ~/
* Strict host key checking must be disabled when using scp
Example:

```
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```
In this example, I:

* remotely execute the ls ~/ command via ssh to see what ~/ contains
* create a file named some_page.html
* execute my 0-transfer_file script
* remotely execute the ls ~/ command via ssh to see that the file some_page.html has been successfully transferred
That is one way of publishing your website pages to your server.

### [1. Install nginx web server](./1-install_nginx_web_server)
![meme0](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/nginx-master-yoda.jpg)
Readme:

* [-y on apt-get command](https://intranet.hbtn.io/rltoken/qU2tVilKLygFZcRpEWD3lw)
Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

* Install nginx on your web-01 server
* Nginx should be listening on port 80
* When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Holberton School
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements
Example:

```
sylvain@ubuntu$ curl 34.198.248.145/
Holberton School for the win!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
```
In this example 34.198.248.145 is the IP of my web-01 server. If you want to query the Nginx that is locally installed on your server, you can use curl 127.0.0.1.

If things are not going as expected, make sure to check out Nginx logs, they can be found in /var/log/.

### [2. Setup a domain name](./2-setup_a_domain_name)
[.TECH Domains](https://intranet.hbtn.io/rltoken/yRrwiHrS15iQQZku72p0aQ) is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your [tools space](https://intranet.hbtn.io/rltoken/F0ZPUs7ODLLwp8lr-um8Xg). Feel free to drop a thank you tweet for [.TECH Domains](https://intranet.hbtn.io/rltoken/d9XjYlM-CqTRHJEcaKpcVQ).

Provide the domain name in your answer file.

Requirement:

* provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)
* configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)
* go to your [profile](https://intranet.hbtn.io/rltoken/fYvJr4-HV1WPnfB7HCue_Q) and enter your domain in the Project website url field
Example:

```
sylvain@ubuntu$ cat 2-setup_a_domain_name
holbertonschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig holbertonschool.tech

; <<>> DiG 9.10.6 <<>> holbertonschool.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;holbertonschool.tech.      IN  A

;; ANSWER SECTION:
holbertonschool.tech.   7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
```

### [3. Redirection](./3-redirection)
Readme:

* [Replace a line with multiple lines with sed](https://intranet.hbtn.io/rltoken/Afg1zCifjmIygL1se0ghhg)
Configure your Nginx server so that /redirect_me is redirecting to another page.

Requirements:

* The redirection must be a “301 Moved Permanently”
* You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
* Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task
Example:

```
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
```

### [4. Not found page 404](./4-not_found_page_404)
Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

Requirements:

* The page must return an HTTP 404 error code
* The page must contain the string Ceci n'est pas une page
* Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task
Example:

```
sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$
```

### [5. Design a beautiful 404 page](./5-design_a_beautiful_404_page)
Some of my favorites:

* [Digital Ocean](https://intranet.hbtn.io/rltoken/BcOQZUPzoF6sfWd28JAOmA)
* [Github](https://intranet.hbtn.io/rltoken/i56pau9DIG49cBUMBwEcPg)
* [Lego](https://intranet.hbtn.io/rltoken/cm7-ZqHoxVdLwhOc1XGwyg)
* [Blizzard](https://intranet.hbtn.io/rltoken/UCBPyeXYTeLDYh3Bi9NgKA)
* [StickerMule](https://intranet.hbtn.io/rltoken/apZ3b5W6-ms9a49_V0e8cg)
Get creative and impress us!



Note that if you decide to have your creative 404 page as the default one, make sure that it still contains the string Ceci n'est pas une page (otherwise the checker will fail your previous project).

Submit the URL of your 404 page in the field bellow.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

### [6. Install Nginx web server (w/ Puppet)](./7-puppet_install_nginx_web_server.pp)
Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

Requirements:

* Nginx should be listening on port 80
* When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Holberton School
* The redirection must be a “301 Moved Permanently”
* Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements

---

## Author
* **Tim Assavarat** - [tassavarat](https://github.com/tassavarat)
