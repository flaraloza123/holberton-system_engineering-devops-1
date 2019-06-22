# 0x04. Loops, conditions and parsing

## Learning Objectives

General
* How to create SSH keys
* What is the advantage of using  #!/usr/bin/env bash over #!/bin/bash
* How to use while, until and for loops
* How to use if, else, elif and case condition statements
* How to use the cut command
* What are files and other comparison operators, and how to use them

## Usage

* All files were created and compiled on Ubuntu 14.04.4 LTS

---
## Tasks

### [0. Create a SSH RSA key pair](./0-RSA_public_key.pub)
* Create a RSA key pair.
```sh
ssh-keygen -t rsa
```

### [1. For Holberton School loop](./1-for_holberton_school)
* Write a Bash script that displays Holberton School 10 times.
```sh
sylvain@ubuntu$ head -n 2 1-for_holberton_school 
#!/usr/bin/env bash
# This script is displaying "Holberton School" 10 times
sylvain@ubuntu$ ./1-for_holberton_school 
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
```

### [2. While Holberton School loop](./2-while_holberton_school)
* Write a Bash script that displays Holberton School 10 times.
```sh
sylvain@ubuntu$ ./2-while_holberton_school
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
```

### [3. Until Holberton School loop](./3-until_holberton_school)
* Write a Bash script that displays Holberton School 10 times.
```sh
sylvain@ubuntu$ ./3-until_holberton_school
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
```

### [4. If 9, say Hi!](./4-if_9_say_hi)
* Write a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.
  * You must use the if statement
```sh
sylvain@ubuntu$ ./4-if_9_say_hi
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Hi
Holberton School
```

### [5. 4 bad luck, 8 is your chance](./5-4_bad_luck_8_is_your_chance)
* Write a Bash script that loops from 1 to 10 and:
  * displays bad luck for the 4th loop iteration
  * displays good luck for the 8th loop iteration
  * displays Holberton School for the other iterations
  * You must use the while loop (for and until are forbidden)
  * You must use the if, elif and else statements
```sh
sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Holberton School
Holberton School
Holberton School
bad luck
Holberton School
Holberton School
Holberton School
good luck
Holberton School
Holberton School
```

### [6. Superstitious numbers](./6-superstitious_numbers)
* Write a Bash script that displays numbers from 1 to 20 and:
  * displays 4 and then bad luck from China for the 4th loop iteration
  * displays 9 and then bad luck from Japan for the 9th loop iteration
  * displays 17 and then bad luck from Italy for the 17th loop iteration
  * You must use the case statement
```sh
sylvain@ubuntu$ ./6-superstitious_numbers
1
2
3
4
bad luck from China
5
6
7
8
9
bad luck from Japan
10
11
12
13
14
15
16
17
bad luck from Italy
18
19
20
```

### [7. Clock](./7-clock)
* Write a Bash script that displays the time for 12 hours and 59 minutes:
  * display hours from 0 to 12
  * display minutes from 1 to 59
```sh
sylvain@ubuntu$ ./7-clock | head -n 70
Hour: 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
Hour: 1
1
2
3
4
5
6
7
8
9
```

### [8. For ls](./8-for_ls)
* Write a Bash script that displays:
  * The content of the current directory
  * In a list format
  * Where only the part of the name after the first dash is displayed (refer to the example)
  * You must use the for loop (while and until are forbidden)
  * Do not display hidden files
```sh
sylvain@ubuntu$ ls
100-read_and_cut              1-for_holberton_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_holberton_school       7-clock
102-lets_parse_apache_logs    3-until_holberton_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
sylvain@ubuntu$  ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_holberton_school
while_holberton_school
until_holberton_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
```

### [9. To file, or not to file](./9-to_file_or_not_to_file)
* Write a Bash script that gives you information about the holbertonschool file.
  * You must use if and, else (case is forbidden)
  * Your Bash script should check if the file exists and print:
    * if the file exists: holbertonschool file exists
    * if the file does not exist: holbertonschool file does not exist
  * If the file exists, print:
    * if the file is empty: holbertonschool file is empty
    * if the file is not empty: holbertonschool file is not empty
    * if the file is a regular file: holbertonschool is a regular file
    * if the file is not a regular file: (nothing)
```sh
sylvain@ubuntu$ file holbertonschool
holbertonschool: cannot open `holbertonschool' (No such file or directory)
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file does not exist
sylvain@ubuntu$ touch holbertonschool
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file exists
holbertonschool file is empty
holbertonschool is a regular file
sylvain@ubuntu$ echo 'betty' > holbertonschool 
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file exists
holbertonschool file is not empty
holbertonschool is a regular file
sylvain@ubuntu$ rm holbertonschool 
sylvain@ubuntu$ mkdir holbertonschool
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file exists
holbertonschool file is not empty
```

### [10. FizzBuzz](./10-fizzbuzz)
* Write a Bash script that displays numbers from 1 to 100.
  * Displays FizzBuzz when the number is a multiple of 3 and 5
  * Displays Fizz when the number is multiple of 3
  * Displays Buzz when the number is a multiple of 5
  * Otherwise, displays the number in a list format
```sh
sylvain@ubuntu$ ./10-fizzbuzz | head -20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

### [11. Read and cut](./100-read_and_cut)
* help: read


### [12. Tell the story of passwd](./101-tell_the_story_of_passwd)
* 


### [13. Let's parse Apache logs](./102-lets_parse_apache_logs)
* 


### [14. Dig the data](./103-dig_the-data)
* Now that you’ve parsed the Apache log file, let’s sort the data so you can get a better idea of what is going on.

---

## Author
* **Tu Vo** - [tuvo1106@gmail.com](https://github.com/tuvo1106)
