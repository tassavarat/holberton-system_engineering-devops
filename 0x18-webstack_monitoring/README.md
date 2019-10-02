# 0x18. Webstack monitoring

## Learning Objectives

* Why is monitoring needed
* What are the 2 main area of monitoring
* What are access logs for a web server (such as Nginx)
* What are error logs for a web server (such as Nginx)

## Requirements

* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.7) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

### [0. Sign up for Datadog and install datadog-agent](./0-setup_datadog)
For this task head to [https://www.datadoghq.com/](https://intranet.hbtn.io/rltoken/Uho9kxbX9KHCSYAQ-Zl1AQ) and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent. 

![img0](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20191002%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191002T032125Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=05cd35734b9e042138dd01450420f307c5ed56813adaa07ca80d7aa22d1e8100)


* Sign up for Datadog
* Install datadog-agent on web-01
* Create an application key
* Create the answer file 0-setup_datadog with your API key on the first line of the file, and your application key on the second

### [1. Monitor some metrics](./1. Monitor some metrics)
Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check.

![img1](https://intranet.hbtn.io/rltoken/naY47nur2yPJNw8tdACnzQ)


* Set up a monitor that checks the number of read requests issued to the device per second.
* Set up a monitor that checks the number of write requests issued to the device per second.

### [2. Create a dashboard](./2. Create a dashboard)
Now create a dashboard with different metrics displayed in order to get a few different visualizations.

* Create a new dashboard
* Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
* Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use [Datadog’s API](https://intranet.hbtn.io/rltoken/VrzQP39UUFMmAKZx0IZLuw)
