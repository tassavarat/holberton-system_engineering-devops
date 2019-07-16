# 0x06. Regular expression

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
* All your regex must be built for the Oniguruma library

---

### [0. Simply matching Holberton](./0-simply_match_holberton.rb)
![0 output](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/just-match-Holberton.png)
Requirements:

* The regular expression must match `Holberton`
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:

```
sylvain@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
HolbertonHolberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$
```


### [1. Repetition Token #0](./1-repetition_token_0.rb)
![1 output](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-0.png)
Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


### [2. Repetition Token #1](./2-repetition_token_1.rb)
![2 output](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-1.png)
Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


### [3. Repetition Token #2](./3-repetition_token_2.rb)
![3 output](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-2.png)
Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


### [4. Repetition Token #3](./4-repetition_token_3.rb)
![4 output](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-3.png)
Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


### [5. Not quite HBTN yet](./5-beginning_and_end.rb)
Requirements:

* The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:

```
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rbb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
```


### [6. Call me maybe](./6-phone_number.rb)
Requirement:

* The regular expression must match a 10 digit phone number


### [7. OMG WHY ARE YOU SHOUTING?](./7-OMG_WHY_ARE_YOU_SHOUTING.rb)
Requirement:

* The regular expression must be only matching: capital letters
Example:

```
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
```

### [8. Textme](./100-textme.rb)
Requirements:

* Your script should output: `[SENDER],[RECEIVER],[FLAGS]`
  * The sender phone number or name (including country code if present)
  * The receiver phone number or name (including country code if present)
  * The flags that were used


### [9. Pass LinkedIn technical interview level0](./101-passed_linkedin_regex_challenge.jpg)
Requirements:

* Solve LinkedIn regex puzzle: https://engineering.linkedin.com/puzzle
* Provide as an answer file a screenshot containing your contact information, including your Holberton email address
Example:

```
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
```

---

## Author
* **Tim Assavarat** - [tassavarat](https://github.com/tassavarat)
