# 0x11. What happens when you type holbertonschool.com in your browser and press Enter

## Learning Objectives

Being a Full-Stack Software Engineer means you’re comfortable interacting with any layer of the stack.

A way to easily assess this is to simply ask an engineer to explain how a software system works. They can have a general overview of the flow or can choose to dig deep in a certain area.

Let’s practice by exploring the infrastructure side (network, servers, security…) of the question.

<p align="center">
  <img src="http://i.imgur.com/R8R3sqC.png">
</p>

---

### [0. What happens when...](./0-blog_post)
* This question is a classic and still widely used interview question for many types of software engineering position. It is used to assess a candidate’s general knowledge of how the web stack works on top of the internet. One important guideline to begin answering this question is that you should ask your interviewer whether they would like you to focus in on one specific area of the workflow. For a front-end position they may want you to talk at length about how the DOM is rendering. For an SRE position they may want you to go into the load balancing mechanism.
This question is a good test of whether you understand DNS. Many software engineering candidates struggle with this concept, so if you do well on this question, you are already way ahead of the curve. If you take this project seriously and write an excellent article, it may be something that will grab the attention of future employers.

* Write a blog post explaining what happens when you type https://www.holbertonschool.com in your browser and press Enter.
  * DNS request
  * TCP/IP
  * Firewall
  * HTTPS/SSL
  * Load-balancer
  * Web server
  * Application server
  * Database


### [1. Everything's better with a pretty diagram](./1-what_happen_when_diagram)
* Add a schema to your blog post illustrating the flow of the request created when you type https://www.holbertonschool.com in your browser and press Enter.
  * DNS resolution
  * that the request hitting server IP on the appropriate port
  * that the traffic is encrypted
  * that the traffic goes through a firewall
  * that the request is distributed via a load balancer
  * that the web server answers the request by serving a web page
  * that the application server generates the web page
  * that the application server request data from the database

### [2. Contribute!](./2-contribution-to_what-happens-when_github_answer)
* Folks on the Internet have been trying to put together a comprehensive answer to the question. Help them by submitting a pull request. Paste the link in your answer file.
  * The pull request must bring meaningful value (not a typo correction or style improvement)
  * Share the pull request URL in your answer file and in the field below


## Author
* **Tu Vo** - [tuvo1106](https://github.com/tuvo1106)
