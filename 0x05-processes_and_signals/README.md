# 0x05. Processes and signals

## Learning Objectives

General
* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Requirements

* All files are created and compiled on Ubuntu 14.04.4 LTS.
* All files are linted with Shellcheck.

## Tasks

### [0. What is my PID](./0-what-is-my-pid)
* Write a Bash script that displays its own PID.
```sh
sylvain@ubuntu$ ./0-what-is-my-pid
4120
```

### [1. List your processes](./1-list_your_processes)
* Write a Bash script that displays a list of currently running processes.
  * Must show all processes, for all users, including those which might not have a TTY
  * Display in a user-oriented format
  * Show process hierarchy
```sh
sylvain@ubuntu$ ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
root         4  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/0:0]
root         5  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/0:0H]
root         7  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    Feb13   0:03  \_ [rcuos/0]
root         9  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcuob/0]
root        11  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [migration/0]
root        12  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [watchdog/0]
root        13  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [khelper]
root        14  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kdevtmpfs]
root        15  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [netns]
root        16  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [writeback]
root        17  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kintegrityd]
root        18  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [bioset]
root        19  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/u3:0]
root        20  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kblockd]
root        21  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [ata_sff]
root        22  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khubd]
root        23  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [md]
root        24  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [devfreq_wq]
root        25  0.0  0.0      0     0 ?        S    Feb13   0:41  \_ [kworker/0:1]
root        27  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khungtaskd]
root        28  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kswapd0]
root        29  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [vmstat]
root        30  0.0  0.0      0     0 ?        SN   Feb13   0:00  \_ [ksmd]
root        31  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [fsnotify_mark]
root        32  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ecryptfs-kthrea]
root        33  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [crypto]
root        45  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kthrotld]
root        46  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:1]
root        65  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [deferwq]
root        66  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [charger_manager]
root       108  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kpsmoused]
root       125  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [scsi_eh_0]
root       126  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:2]
root       172  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [jbd2/sda1-8]
root       173  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [ext4-rsv-conver]
root       409  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [iprt]
root       549  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/u3:1]
root       808  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kauditd]
root       834  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [rpciod]
root       846  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [nfsiod]
root         1  0.0  0.4  33608  2168 ?        Ss   Feb13   0:00 /sbin/init
root       373  0.0  0.0  19472   408 ?        S    Feb13   0:00 upstart-udev-bridge --daemon
root       378  0.0  0.2  49904  1088 ?        Ss   Feb13   0:00 /lib/systemd/systemd-udevd --daemon
root       518  0.0  0.1  23416   644 ?        Ss   Feb13   0:00 rpcbind
statd      547  0.0  0.1  21536   852 ?        Ss   Feb13   0:00 rpc.statd -L
```

### [2. Show your Bash PID](./2-show_your_bash_pid)
* Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
  * You cannot use pgrep
  * The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)
```sh
sylvain@ubuntu$ sylvain@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
```

### [3. Show your Bash PID made easy](./3-show_your_bash_pid_made_easy)
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
  * You cannot use ps
```sh
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4557 bash
```

### [4. To infinity and beyond](./4-to_infinity_and_beyond)
* Write a Bash script that displays To infinity and beyond indefinitely. 
```sh
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C
```

### [5. Kill me now](./5-kill_me_now)
* We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
* Write a Bash script that kills 4-to_infinity_and_beyond process.
  * You must use kill
```sh
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
```

### [6. Kill me now made easy](./6-kill_me_now_made_easy)
* Write a Bash script that kills 4-to_infinity_and_beyond process.
  * You cannot use kill or killall

Terminal 0
```sh
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
```

Terminal 1
```sh
sylvain@ubuntu$ ./6-kill_me_now_made_easy
```

### [7. Highlander](./7-highlander)
* Write a Bash script that displays: 
  * To infinity and beyond indefinitely
  * With a sleep 2 in between each iteration
  * I am invincible!!! when receiving a SIGTERM signal
* Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

Terminal 0
```sh
sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
^C
```

Terminal 1
```sh
sylvain@ubuntu$ ./67-kill_me_now_made_easy 
sylvain@ubuntu$ ./67-kill_me_now_made_easy
sylvain@ubuntu$ ./67-kill_me_now_made_easy
```
* I started 7-highlander in Terminal #0 and then run 67-kill_me_now_made_easy in terminal #1, for every iteration we can see I am invincible!!! appearing in terminal #0.

### [8. Beheaded process](./8-beheaded_process)
* Write a Bash script that kills the process 7-highlander.

Terminal 0
```sh
sylvain@ubuntu$ ./7-highlander 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
```

Terminal 1
```sh
sylvain@ubuntu$ ./8-beheaded_process
```

* I started 7-highlander in Terminal #0 and then run 8-beheaded_process in terminal #1 and we can see that the 7-highlander has been killed.

### [9. Process and PID file](./100-process_and_pid_file)
* Write a Bash script that: 
  * Creates the file /var/run/holbertonscript.pid containing its PID
  * Displays To infinity and beyond indefinitely
  * Displays I hate the kill command when receiving a SIGTERM signal
  * Displays Y U no love me?! when receiving a SIGINT signal
  * Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
```sh
sylvain@ubuntu$ sudo ./100-process_and_pid_file
To infinity and beyond
To infinity and beyond
^CY U no love me?!
```

Executing the 100-process_and_pid_file script and killing it with ctrl+c.

```sh
sylvain@ubuntu$ sudo ./100-process_and_pid_file
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
I hate the kill command
```

Terminal 1

```sh
sylvain@ubuntu$ sudo pkill -f 100-process_and_pid_file
```

Starting 100-process_and_pid_file in the terminal #0 and then killing it in the terminal #1.

### [10. Manage my process](./101-manage_my_process)
* Write a manage_my_process Bash script that:
  * Indefinitely writes I am alive! to the file /tmp/my_process
  * In between every I am alive! message, the program should pause for 2 seconds
  * Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)
* Requirements:
  * When passing the argument start:
    * Starts manage_my_process
    * Creates a file containing its PID in /var/run/my_process.pid
    * Displays manage_my_process started
  * When passing the argument stop:
    * Stops manage_my_process
    * Deletes the file /var/run/my_process.pid
    * Displays manage_my_process stopped
  * When passing the argument restart
    * Stops manage_my_process
  * Deletes the file /var/run/my_process.pid
    * Starts manage_my_process
    * Creates a file containing its PID in /var/run/my_process.pid
    * Displays manage_my_process restarted
  * Displays Requirements: manage_my_process {start|stop|restart} if any other argument or no argument is passed
```sh
sylvain@ubuntu$ sudo ./101-manage_my_process
Requirements: manage_my_process {start|stop|restart}
sylvain@ubuntu$ sudo ./101-manage_my_process start
manage_my_process started
sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
I am alive!
I am alive!
I am alive!
I am alive!
^C
sylvain@ubuntu$ sudo ./101-manage_my_process stop
manage_my_process stopped
sylvain@ubuntu$ cat /var/run/my_process.pid 
cat: /var/run/my_process.pid: No such file or directory
sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
^C
sylvain@ubuntu$ sudo ./101-manage_my_process start
manage_my_process started
sylvain@ubuntu$ cat /var/run/my_process.pid 
11864
sylvain@ubuntu$ sudo ./101-manage_my_process restart
manage_my_process restarted
sylvain@ubuntu$ cat /var/run/my_process.pid 
11918
sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
I am alive!
I am alive!
I am alive!
^C
```

### [11. Zombie](./102-zombie.c)
* Write a C program that creates 5 zombie processes.
  * For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
  * Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
  * When your code is done creating the parent process and the zombies, use the function bellow
```c
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```

Terminal #0

```sh
sylvain@ubuntu$ gcc 102-zombie.c -o zombie
sylvain@ubuntu$ ./zombie 
Zombie process created, PID: 13527
Zombie process created, PID: 13528
Zombie process created, PID: 13529
Zombie process created, PID: 13530
Zombie process created, PID: 13531
^C
```

Terminal 1

```sh
sylvain@ubuntu$ ps aux | grep -e 'Z+.*<defunct>'
sylvain  13527  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13528  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13529  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13530  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13531  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13533  0.0  0.1  10460   964 pts/2    S+   01:19   0:00 grep --color=auto -e Z+.*<defunct>
```

In Terminal #0, I start by compiling 102-zombie.c and executing zombie which creates 5 zombie processes. In Terminal #1, I display the list of processes and look for lines containing Z+.*<defunct> which catches zombie process.

### [12. Screencast](./103-screencast_unix_signal)
* Create a screencast where you live-code/demo something related to Unix signals.
  * Step by step video
  * Two minutes of above
  * Done in English
  * Published to Youtube

## Author
* **Tu Vo** - [tuvo1106](https://github.com/tuvo1106)
