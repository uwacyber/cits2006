# Lab 0: Setup, Linux and Networking

Coming soon...

## 0.1 Linux refresher

This lab is to provide a refresher on your Linux knowledge, and you can do this on your Kali VM. You may skim/skip through this lab if you feel confident, but if you haven't done much in Linux for a while (a semester or two), you are strongly advised to complete this lab before moving on to other labs to improve your workflow efficiency. For each example, you should try it yourself before moving on to the next section.

### 0.1.1. Distributions

The base system of Linux comes in many different distributions which contain different packages and features written by different groups. These are referred to as distros for short, and they have a wide variety of different uses, purposes, systems, features, and fan bases. This guide will attempt to be distro-independent, however, a few of the more popular distros are listed:

| <p>· Ubuntu</p><p>· Debian</p><p>· Fedora</p><p>· Linux Mint</p> | <p>· Red Hat</p><p>· CentOS</p><p>· Arch Linux</p><p>· Gentoo</p> |
| ---------------------------------------------------------------- | ----------------------------------------------------------------- |

### 0.1.2. Package manager and repositories

Each distribution comes with a package manager, which handles software installed on the system and has a number of remote repositories from which it gets its software. For example, Ubuntu (also Kali) uses a package manager called aptitude (apt for short). You can type:

`sudo apt-get install firefox`

to install the Mozilla Firefox web browser. It will search the remote repositories (listed in `/etc/apt/-sources.list`) for the required packages and instructions to install them and once found, it will install the software on your computer for you. The package manager can also update and remove software, and manage your local package database. This is one of the brilliant things of a package manager: you can run a single command and you've installed new software - You can run a single command, and update all your packages, etc.

{% hint style="info" %}
`apt-get` is the package manager for Ubuntu. Fedora uses `dnf` (previously `yum`), Arch uses `pacman`, and Debian uses aptitude, etc. For instance:

`dnf install firefox`

will install Firefox on a Fedora machine. You can also install multiple package managers on any one distro, but as they say\_: too many cooks spoil the broth\_.
{% endhint %}

### 0.1.3. The Terminal

**0.1.3.1. Commands**

Firstly you should get familiar with the man pages, which are essentially the manual, and will display help pages on almost all commands.

`Usage: man COMMAND`

Where COMMAND is replaced with whatever command you want help on. Press '`q`' to exit a manual page. Alternatively, most commands will allow you to add `--help` on the end to get their own personal help pages. Here is a list of the essential commands that you should become familiar with (and you can use the manual to learn how to use them):

`cd ------ # Change directory`\
`ls ------ # Show contents of directory`\
`echo ---- # Print text to the screen`\
`cat ----- # Display contents of a file`\
`nano ---- # Edit a file via the command line`\
`mv ------ # Move (or rename) a file`\
`cp ------ # Copy a file`\
`rm ------ # Remove (delete) a file`

These are some extra commands which aren't totally essential but are certainly helpful:

`mkdir --- # Make a new directory`\
`rmdir---- # Delete a directory`\
`grep ---- # Search for specific text within text`\
`pwd ----- # Print working (current) directory`\
`whoami -- # Display user`\
`ps ------ # Display running processes`\
`pstree -- # Display a tree showing running processes and processes they started`\
`top ----- # Display most intensive running programs`\
`who ----- # Display logged on users`\
`w ------- # Display logged on users`\
`which --- # Display the path to a command's binary`\
`df ------ # Disk space free`\
`du ------ # Disk space used`\
`passwd -- # Change user password (not to be confused with pwd)`\
`more ---- # Display text one screenful at a time`\
`less ---- # Display text one screenful at a time`\
`wc ------ # Word/letter/byte count`\
`id ------ # Display the uid, gid and groups of a user`\
`su ------ # Switch user`\
`tty ----- # Display which tty you are on`

####

#### **0.1.3.2. Shortcuts**

Every key pressed ends a character to the terminal, and you can send different characters by holding down keys like \[Ctrl] or \[Alt]. This is how the shell can tell what key is pressed, and thus, allow shortcuts to be defined. Some of the more useful keyboard shortcuts are defined:

* `Up or Down arrows :` Scroll through typed commands
* `Home or End :` Move to the start or end of a line, respectively
* `Tab :` Autocomplete a file name, directory name or command name.
* `Ctrl + C :` End a running process
* `Ctrl + D :` End an End-Of-File (EOF) character (usually ends a process or signifies the end of input data)
* `Ctrl + Z :` Send the currently running process to the background
* `Ctrl + L :` Clear the screen, same as running the clear command

####

#### 0.1.3.3. **Piping and redirection**

There are a number of little quirks that the shell has that gives it more functionality. Piping takes the `stdout` of the left program and connects it (i.e. _pipes_ it) into `stdin` of the right program with the pipe operator `|`. For example:

`# Count number of words in helloworld.txt`\
`cat helloworld.txt | wc -w`

Redirection directs data in and out of files, i.e.

`# Redirect stdout to file`\
`echo "Hello world" > helloworld.txt`\
``\ `# Redirect stdout to the end of a file`\ `echo "world." >> hello.txt`\``\
`# Redirect a file to stdin`\
`more < helloworld.txt`

####

#### **0.1.3.4. Wildcards**

The shell uses a number of special characters called wildcards, similar to regular expressions or regex, which can be used to manipulate what is being dealt with on the command line. The standard wildcards are thus:

`*` Match 0 or more characters. For example, `rm *.txt` will delete all files that end in .txt, and `cp somedirectory/* .` will copy all files from \`somedirectory' to the current directory.

`?` Match any single character. For example, `cp example.?` will copy all files named \`example' with a single character extension, into the directory \`somedir'

`[]` Match any single character in the square brackets. You can even specify a range, i.e. `rm m[a-e]m` will delete any files starting and ending with `m`, and with any letter between \`a' and \`e' in between. `rm m[abc]m` will delete files \`mam', \`mbm', \`mcm'.

`{}` Match any item in the braces. For example, `cp {*.doc,*.pdf} ~` copies any files with the extension \`.doc' or \`.pdf' to the home directory.

**0.1.3.5. Conditional execution**

You can chain commands together on one line by separating them with a semicolon \`;'.

`cmd1; cmd2; cmd3`

However, every program returns a number back to the OS once it has finished running to tell if it was completed successfully or not, and we can use this to chain execute commands conditionally.

To run a command if and only if the last command completed successfully, we use `&&`:

`user@MY-PC:~$ mkdir foo && cd foo && echo "hooray" > somefile`\
`user@MY-PC:~/foo$ cat somefile`\
`hooray`\
`user@MY-PC:~/foo$`

To run a command if and only if the last command failed, we use `||`:

`user@MY-PC:~$ ls foo || cd foo || mkdir foo && ls -ld foo`\
`ls: cannot access foo: No such file or directory`\
`bash: cd: foo: No such file or directory`\
`drwxrwxr-x 2 user user 4096 May 24 00:57 foo`

#### **0.1.3.6. Processes**

Every program that runs, runs in virtual memory as a process, even the shell. You can list the currently running processes with the command `top`. When you run a command, the terminal session runs it on its process, waits for it to complete, then regains control once the command is finished. So, if you were to close the terminal window while a command was running, that would stop the command. Since this can be inconvenient, we can \`fork' the command into its own process to run in the background, and still use the shell while it runs (which is useful for commands that take a long time). To do this, we end the command with a single ampersand `&`. For example:

`user@MY-PC:~$ (sleep 15; date) & date`\
`[1] 12186`\
`Thu May 24 02:06:14 AWST 2022`\
`user@MY-PC:~$`\
`user@MY-PC:~$ Thu May 24 02:06:29 AWST 2022`\
\`\`\
`[1]+ Done ( sleep 15; date )`\
`user@MY-PC:~$`

`(sleep 15; date)` is sent to the background and returns the process ID (PID), then the next date is run and the shell is returned. After sleeping for 15 seconds, the date sent to the background outputs and the shell reports that the command completed.

There is a command, `nohup` (no hangup), which prevents a program from being forcefully terminated under normal circumstances. We can combine this with `&` to run programs that need to run uninterrupted for long periods of time.

Another way to list the processes running is with `ps`, and then end them with `killall` (kill by process name), or with `pkill` (kill by process ID), or even with the keyboard shortcut \[Ctrl] + \[C] as mentioned above. Check the man page, as well as \[8] for more options.

You can also check what is running in the background and foreground with `bg` and `fg`, respectively.

### 0.1.4. File system structure

The file system is structured as a tree that flows down from the root directory, which is simply represented as /. Below shows an example listing of a system’s root directory using the ls command:

`user@MY-PC:~$ ls /`\
`bin etc initrd.img.old lost+found proc selinux usr`\
`boot fixdm lib media root srv var`\
`cdrom home lib32 mnt run sys vmlinuz`\
`dev initrd.img lib64 opt sbin tmp vmlinuz.old`

The standard path is listed as all the directories to a file, separated by the `/` character. You can also use `..` to represent the folder that the current folder is in, `.` to represent the current directory, and `~` to represent your home directory. For example

`# Move two folders up, then into dir1 and then dir2, then back into dir1, then back into dir2`\
`cd ../../dir1/dir2/../dir2`\
`# Get a listing of the current directory`\
`ls .`\
`# Change into your home directory`\
`cd ~`

Linux will automatically complete a command or filename if you are part-way through typing it; all you have to do is hit the \[Tab] key. Press \[Tab] enough times and it will list possible suggestions based on what you currently have typed in the terminal.

#### \*\*\*\*

#### **0.1.4.1. File operations**

There are a number of useful programs that allow us to do file manipulation. To list some of the main operations:

|   `cp` | Copy a file from one location to the other.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   `mv` | Move a file from one location to the other. Note, this is also used to rename files - you just \`move' the file to the directory it is already in but as a new name, for example `mv foo bar` would rename the file from \`foo' to \`bar', assuming you didn't have a directory named \`bar', in which case, the file would be moved to that directory instead.                                                                                                                                              |
|   `rm` | Delete a file. Note that you can also delete empty directories this way, and you can delete a directory and its subdirectories by using `rm -r`. However, be **VERY** careful: if you were to run `rm -rf /`, you would erase every file on your whole computer, because it would delete the root directory and then every file and subdirectory below it and it wouldn't stop because the \`f' in \`-rf' means \`force'. Use `rm -rf` with extreme caution, or even use `rmdir`, which removes a directory. |
| `grep` | grep stands for Global Regular Expressions Parser, and can search through text for a match. For example, `grep foo bar` searches the file bar for the string foo, and you can also use `ls -l \| grep "foo"`, which searches the file listing for a file called foo. When combined with `sed` and `awk`, you can do almost anything string related.                                                                                                                                                          |

#### **0.1.4.2. $PATH and the environment**

Variables in the shell are defined using the export command, and when variables are used, they start with a `$`.\
\
`user@MY-PC:~$ export FOO="This is a string"`\
`user@MY-PC:~$ echo $FOO`\
`This is a string`

You can see a list of the set environment variables by typing `set` by itself into the terminal.

Linux uses a global terminal variable to find programs. This is the $PATH variable and it consists of a list of file paths to search in for a specified program, in order, separated by the colon (:). For example, a listing of my path:

`user@MY-PC:~$ echo $PATH`\
`/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games`

This would mean that if I were to use the command `ls`, it would search for a binary file called 'ls' in `/usr/local/sbin`, then in `/usr/local/bin`, and so on until it found it. Then it would be executed. Because these are searched in order, if you were to prepend a directory path to the front of `$PATH` with your own copy of `ls` in it, and then run the ls command, then your copy would be run instead.

This is sometimes used as an exploit by modifying the user's `$PATH` variable so that a path containing malicious binaries with the same names as common commands is on the front. When the user runs these commands, then the malicious binaries are run instead.

### 0.1.5. Users and Permissions

Every user has a user ID (uid) and a group ID (gid). Each user also has a list of groups they are a part of which give them the permissions that are assigned to those groups. You can see this by using the 'id' command:\
\
`user@MY-PC:~$ id`\
`uid=1000(user)gid=1000(user)groups=1000(user),4(adm),24(cdrom),27(sudo),29(audio),30(dip),44(video),46(plugdev),109(lpadmin),119(pulse),124(sambashare)`

#### \*\*\*\*

#### **0.1.5.1. sudo and root**

Now for the most powerful user on Linux: The root user. Root's uid and gid are both 0.

`user@MY-PC:~$ id root`\
`uid=0(root) gid=0(root) groups=0(root)`

The root account can do anything, while other accounts would be denied due to the lack of permissions required. Root is the first account created on a newly installed Linux distro, and it is generally encouraged that you do not use the root account unless you absolutely have to because since root can do anything, then there's no stopping you from accidentally deleting something important.

This is where the `sudo` command comes in (a.k.a "super-user do"). You can use `sudo` to execute commands that require elevated privileges without having to actually switch to root.

Say you want to edit the hostname file, which contains the name of your computer, but, by default, you need elevated privileges to edit it. You would type:

`sudo nano /etc/hostname`

to which it asks you for your password, and then opens nano with the extra privileges provided by `sudo`. There is a `sudoers` file which contains a list of users who can use `sudo`, and what privileges they get from using it.

#### **0.1.5.2. File permissions**

Linux inherits its file permissions system from Unix. You can use the command `ls -l` to display the permissions of a file or files:

`user@MY-PC:~/junk$ ls -l`\
`total 8`\
`-rw-rw-r-- 1 user user 9 Apr 25 21:28 junk1`\
`drwxrwxr-x 2 user user 4096 Apr 25 21:29 other_junk`

The first string consists of a sequence of letters, which represent the permissions on the file. The two names refer to the owner and group the file belongs to, respectively.

Let's take the file, `junk1`, as our example. The first character is the file type. This is a \`d' if the file is a directory (like `other_junk`). The next part should be read as three sets of permissions

`-rw-rw-r--`\
`( d )( u )( g )( o )`\
`( - )(rw-)(rw-)(r--)`

where the first set, `u`, refers to the permissions for the user who owns the file. The next set, `g`, refers to the permissions for the group that the file belongs to. The final set, `o`, refers to the permissions for any other user. Each set uses \`rwx' to specify the permission to (r)ead, (w)rite or e(x)ecute, or `-` if that permission is not set. Let’s take a look at the folder `other_junk`.

`drwxrwxr-x`

This is a directory, the user has read/write/execute access, users belonging to the group of the file have read/write/execute access, and everyone else has read/execute access, but not write access.

#### **0.1.5.3. Changing permissions**

If you want to change a file's permissions, you can use `chmod`, meaning "change mode". There are two ways to do this: using u/g/o and +/- r/w/x:\
\
`chmod o+x junk1 # Add execute permission to others`\
`chmod og+wx junk1 # Add execute and write permissions to other and group`\
`chmod +x junk1 # Make junk1 executable for the user`\
`chmod g-w junk1 # Remove write permissions from junk1 for group`

etc...

or with a number that represents permissions, called a bitmask. This will set all the permissions at once for you.

`user@MY-PC:~/junk$ chmod 755 junk1`\
`user@MY-PC:~/junk$ ls -l`\
`total 8`\
`-rwxr-xr-x 1 user user 9 Apr 25 21:28 junk1`\
`drwxrwxr-x 2 user user 4096 Apr 25 21:29 other_junk`

The bit mask is three digits (sometimes four digits) between the numbers 0 and 7. Each digit represents what the read/write/execute permissions would be in binary. Take a look:

`0 = 000 = ---`\
`1 = 001 = --x`\
`2 = 010 = -w-`\
`3 = 011 = -wx`\
`4 = 100 = r--`\
`5 = 101 = r-x`\
`6 = 110 = rw-`\
`7 = 111 = rwx`

So, as a few examples,

`777 = rwxrwxrwx`\
`755 = rwxr-xr-x`\
`132 = --x-wx-w-`\
`564 = r-xrw-r--`\
`000 = ---------`

etc...

So when we set our file junk1 to 755 earlier, we set it to rwxr-xr-x, which is a pretty good permission set on your average file. Realistically, you will usually always have your own user permissions set to rwx or rw-, otherwise you are just inconveniencing yourself. You can also use `chown` to change ownership of a file.

### 0.1.6. Network commands

#### 0.1.6.1. ping

* Can be a handful for DNS checks (up / or down) | is a DNS tool to resolve web addresses to an IP address.
* Test reachability - determine round-trip time, and uses ICMP protocol.

```
~#: ping www.google.com 

PING www.google.com (172.217.168.164): 56 data bytes
64 bytes from 172.217.168.164: icmp_seq=0 ttl=55 time=25.981 ms
64 bytes from 172.217.168.164: icmp_seq=1 ttl=55 time=25.236 ms
--- www.google.com ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 25.236/25.608/25.981/0.373 ms
```

#### 0.1.6.2. netstat

* Network statistics
* Get info on host system TCP / UDP connections and status of all open and listening ports and routing table.
* Who are you talking to?
* Who is trying to talk to you?

```
netstat -a # (show all active connections) (servers)
netstat -n # (hosts)
netstat -b # (Show binaries Windows)
```

#### 0.1.6.3. traceroute

* Traceroute - how packets get from the host to another endpoint. Traceroute is helpful to see what routers are being hit, both internal and external.
* **Take advantage of ICMP Time to Live (TTL) Exceeded error message**
  * The time in TTL refers to hops, not seconds or minutes.
  * TTL=1 is the first router.
  * TTL=2 is the second router, and so on.

![](https://2.bp.blogspot.com/-bJD787kOoXg/WxfnpFe4tVI/AAAAAAAAXN4/XTCxg0nFEAQOjtEVcvDzL2N-pK-EbQA2wCLcBGAs/s1600/0.png)

* _As shown above, on HOP 2 the TTL exceeded and back to device A, counting 3 on TTL for the next HOP._

```
~#: traceroute google.com

traceroute to google.com (172.217.17.14), 64 hops max, 52 byte packets
 1  192.168.1.1 (192.168.1.1)  4.960 ms  3.928 ms  3.724 ms
 2  10.10.124.254 (10.10.127.254)  11.175 ms  14.938 ms  15.257 ms
 3  10.133.200.17 (10.137.201.17)  13.212 ms  12.581 ms  12.742 ms
 4  10.255.44.86 (10.255.45.86)  16.369 ms  15.100 ms  17.488 ms
 5  71.14.201.214 (71.14.201.214)  13.287 ms  29.262 ms  16.591 ms
 6  79.125.235.68 (79.125.242.68)  22.488 ms
    79.125.235.84 (79.125.242.84)  13.833 ms *
 7  79.125.252.202 (79.125.252.202)  24.147 ms
    108.170.252.241 (108.170.25@.241)  26.352 ms
    79.125.252.202 (79.125.252.202)  23.598 ms
 8  108.170.252.247 (108.170.252.247)  31.187 ms
    79.125.252.199 (79.121.251.191)  22.885 ms
```

#### 0.1.6.4. arp

* Address resolution protocol - caches of ip-to-ethernet
* Determine a MAC address based on IP addresses
* Option `-a`: view local ARP table

```
~#: arp -a

? (192.168.1.3) at 00:11:22:33:44:55 [ether] on enp0s10
? (192.168.1.128) at e8:33:b0:70:2c:71 [ether] on enp0s10
? (192.168.1.4) at 2c:33:5c:a4:2e:8a [ether] on enp0s10
_gateway (192.168.1.1) at 00:31:33:8b:2a:da [ether] on enp0s10
```

#### 0.1.6.5. ifconfig

* Equivalent to ipconfig in Windows for UNIX/Linux OS.

```
~#: ifconfig
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 00:11:22:33:44:55  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enp0s10: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.128  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::acf6:2ae2:ab5c:6316  prefixlen 64  scopeid 0x20<link>
        ether aa:bb:cc:dd:ee:ff  txqueuelen 1000  (Ethernet)
        RX packets 156651  bytes 29382856 (28.0 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 76400  bytes 23111524 (22.0 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

#### 0.1.6.6. iwconfig

similar to ifconfig, but is dedicated to the wireless network interface.

```
~#: iwconfig
lo        no wireless extensions.

enp0s10   no wireless extensions.

wlp3s0b1  IEEE 802.11  ESSID:off/any  
          Mode:Managed  Access Point: Not-Associated   Tx-Power=19 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:off
          
docker0   no wireless extensions.
```

#### 0.1.6.7. ip addr

show / manipulate routing, network devices, interfaces and tunnels.

Show all the ip configuration, mac address, ipv6 etc.

```
~#: ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s10: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether aa:bb:cc:dd:ee:ff brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.111/24 brd 192.168.1.255 scope global dynamic noprefixroute enp0s10
       valid_lft 4761sec preferred_lft 4761sec
    inet6 fe80::acf6:2ae2:ab5c:6316 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

#### 0.1.6.8. nslookup

* Query Internet name servers interactively; check if the DNS server is working

```
nslookup www.certifiedhacker.com

output:
Server:         192.168.1.1
Address:        192.168.1.1#53

Non-authoritative answer:
www.certifiedhacker.com canonical name = certifiedhacker.com.
Name:   certifiedhacker.com
Address: 162.241.216.11 inslookup www.certifiedhacker.com
Server:         192.168.1.1
Address:        192.168.1.1#53

Non-authoritative answer:
www.certifiedhacker.com canonical name = certifiedhacker.com.
Name:   certifiedhacker.com
Address: 162.241.216.11
```

#### 0.1.6.9. dig

* DNS lookup tool - Functions like `nslookup`, but allows for further functionality.

```
dig www.certifiedhacker.com

output:
; <<>> DiG 9.11.14-3-Debian <<>> certifiedhacker.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 15708
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 2048
; COOKIE: 71bd915b07b3fd08757c9ad65e5d6f3e549d5187359e97cb (good)
;; QUESTION SECTION:
;certifiedhacker.com.           IN      A

;; ANSWER SECTION:
certifiedhacker.com.    14400   IN      A       162.241.216.11

;; Query time: 419 msec
;; SERVER: 192.168.1.1#53(192.168.1.1)
;; WHEN: Mon Mar 02 15:40:29 EST 2020
;; MSG SIZE  rcvd: 92
```

#### 0.1.6.10. netcat

TCP/IP swiss army knife; you can make any type of connection and see the results from a command line. With `nc` you can connect to anything on any port number or you can make your system listen on a port number. Can be an aggressive tool for recon.

![](https://www.researchgate.net/publication/329745450/figure/fig3/AS:705181092179978@1545139682702/Remote-Command-and-Control-example-through-Netcat.ppm)

* "Read" or "Write" to the network
  * Open a port and send or receive some traffic
  * Listen on a port number
  * Transfer data
  * Scan ports and send data to a port
* Become a backdoor
  * Run a shell from a remote device



### Need more practice?

Please have a look at the below links for more UNIX tutorials.

* [http://www.ee.surrey.ac.uk/Teaching/Unix/](http://www.ee.surrey.ac.uk/Teaching/Unix/)
* [https://www.sporcle.com/games/sporcilicious/common\_linux\_commands](https://www.sporcle.com/games/sporcilicious/common\_linux\_commands)
* [https://0xax.gitbooks.io/linux-insides/?fbclid=IwAR1UOzoLvB-OKfCpLcxB0JMy-6GBkKVRZnSdgxydoW8jJLgjAX9BiKHKzf8](https://0xax.gitbooks.io/linux-insides/?fbclid=IwAR1UOzoLvB-OKfCpLcxB0JMy-6GBkKVRZnSdgxydoW8jJLgjAX9BiKHKzf8) 




# Background: Networks 101

{% hint style="info" %}
Go through this if you need a refresher on Computer Networks. Otherwise skip.
Credits to #Samsar4@Github for preparing the materials.
{% endhint %}

> ⚠ Networking 101 is a simple introduction to the most important network concepts for ethical hacking. This is a huge subject and is recommended to learn from different sources like courses, books and certifications like [Cisco CCNA](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html) or [CompTIA Network+](https://www.comptia.org/certifications/network). Also there is a ton of **free training** out there, I recommend to [check this list](https://freetraining.dfirdiva.com/free-networking-training) later.

#### Objectives

* Understand network basic concepts

#### **This module follows the order:**

1. Introduction
2. IP and MAC Addresses
3. Subnetting
4. TCP, UDP and 3-Way-Handshake
5. Ports & Protocols
6. OSI Model

## 1. Introduction

### So, what the heck is a Network?

A network consists of two or more computers that are linked in order to share resources. Computer networks are the basis of communication in IT. They are used in a huge variety of ways and can include many different types of network. A computer network is a set of computers that are connected together so that they can share information. The earliest examples of computer networks are from the 1960s, but they have come a long way in the half-century since then.

![net](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/5edc8fbef915a17c93fa91c95877134c8fac324c/net2.jpg)

LAN Network Topology - SOHO / Small Home Network

**Two very common types of networks include: LAN (Local Area Network) and WAN (Wide Area Network)**

### Topologies

There are many different types of network, which can be used for different purposes and by different types of people and organization. Here are some of the network types that you might come across:

#### LAN - Local Area Network

* A LAN is a network that has a logical and physical borders that a computer can broadcast

![](https://www.geocities.ws/alcantara97/starhttt.gif)

#### WAN - Wide Area Network

* WAN is a multiple LANs or additional WANs with routing functionality for interconnectivity.

![](https://gist.github.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/a3f9b5f3f243467208da83e0d0e543b32233c5d6/wan-topo.jpg)

#### MAN - Metropolitan Area Network

![](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/f37cec4e00f726cb4be3661f20ccad77751e003a/man-topo.jpg)

#### Internet

Connecting WANs through WANs until complete the entire world = Internet.

* The protocol which runs the internet is TCP/IP
* As long you're using legitimate IPv4 address or IPv6

![](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/8c176b8a798fb5749c4391c45015ee5d14d56f13/internet.png)

#### Intranet

If you're using the TCP/IP stack and making your own LAN or WAN = Intranet.

* Intranet is a private network which still runs TCP/IP

![](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/8c176b8a798fb5749c4391c45015ee5d14d56f13/intranet.png)

### Common Terms in Networking

* **IP (internet protocol) address**: the network address of the system across the network, which is also known as the Logical Address).
* **MAC address**: the MAC address or physical address uniquely identifies each host. It is associated with the Network Interface Card (NIC).
* **Open system**: an open system is connected to the network and prepared for communication.
* **Closed system**: a closed system is not connected to the network and so can't be communicated with.
* **Port**: a port is a channel through which data is sent and received.
* **Nodes**: nodes is a term used to refer to any computing devices such as computers that send and receive network packets across the network.
* **Network packets**: the data that is sent to and from the nodes in a network.
* **Routers**: routers are pieces of hardware that manage router packets. They determine which node the information came from and where to send it to. A router has a routing protocol which defines how it communicates with other routers.
* **‍Network address translation (NAT)**: a technique that routers use to provide internet service to more devices using fewer public IPs. A router has a public IP address but devices connected to it are assigned private IPs that others outside of the network can't see.
* **Dynamic host configuration protocol (DHCP)**: assigns dynamic IP addresses to hosts and is maintained by the internet service provider.
* **Internet service providers (ISP)**: companies that provide everyone with their internet connection, both to individuals and to businesses and other organizations.

## 2. IP & MAC Address

### What is an IP Address (Internet Protocol)?

![ip](https://media.fs.com/images/community/upload/wangEditor/201912/24/\_1577182449\_2uLs0pQcuT.jpg)

An IP address is a unique address that identifies a device on the internet or a local network. IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network.

### Check your local IP address

1. If you are using Linux or MacOS you can open your terminal and type `ifconfig` command
2. For Windows machine you can open up the cmd prompt or powershell, then type `ipconfig /all`

![inet](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/5a56240010acbc33026413ad6b5c6f66e9450413/inet.png)

* inet IPv4: `192.168.64.3`
  * `inet` --> The inet (Internet protocol family) show the local IP address. This is IP version 4 (IPv4) Using 32-bit decimal number.
* inet6 IPv6: `fe80::c83b:ccff:fe0e:1069`
  * `inet6` --> Is a new version of IP (IPv6), using 128 bits hexadecimal value.
* `ether` --> MAC address - unique identifier assigned to a network interface controller (NIC)

### More about the IPv4 decimal value:

```
IPv4 = 32 bits range (4 octets of 8 bits, from 0-255 each(4))

11000000.10101000.01000000.00000011   [IPv4 binary]
   192  .   168  .   64   .  3        [IPv4 decimal]
```

#### The arithmetic behind IPv4:

* One octet have 8 bits:

| 0 or 1    | 0 or 1   | 0 or 1   | 0 or 1   | 0 or 1  | 0 or 1  | 0 or 1  | 0 or 1  |
| --------- | -------- | -------- | -------- | ------- | ------- | ------- | ------- |
| 8th bit   | 7th bit  | 6th bit  | 5th bit  | 4th bit | 3rd bit | 2nd bit | 1st bit |
| 128 (2^7) | 64 (2^6) | 32 (2^5) | 16 (2^4) | 8 (2^3) | 4 (2^2) | 2 (2^1) | 1 (2^0) |

Here is how binary octets convert to decimal: The right most bit, or least significant bit, of an octet holds a value of 2^0. The bit just to the left of that holds a value of 2^1. This continues until the left-most bit, or most significant bit, which holds a value of 2^7. So if all binary bits are a one, the decimal equivalent would be 255 as shown here:

```
  1   1   1   1   1   1   1   1
  |   |   |   |   |   |   |   |
(128 +64 +32 +16 +8  +4  +2  +1) --> 255 

Example of octet conversion:
IP Address: 192.168.64.3

To calculate the first octet (192.), from binary format to decimal:

128  64  32  16  8   4   2   1         
 |   |   |   |   |   |   |   |
 1   1   0   0   0   0   0   0          
 |   |   |   |   |   |   |   |
128+ 64+ 0+  0+  0+  0+  0+  0 = 192   ---> final value (firt octet IPv4 in decimal)
```

* Take the IP: `192.168.64.3`
* The first octet `192` in 8-bit binary is `11000000`.
* Only the `8th` and `7th` bit is on and the rest of them (`6th to 1st bit`) is off, meaning the decimal value is the final sum of these values: `128 + 64 = 192`

⚠️ **Why? Computers see everything in terms of binaryll; on and off.**

### IPv4 and IPv6

![ipv](https://academy.avast.com/hs-fs/hubfs/New\_Avast\_Academy/IPv4%20vs.%20IPv6%20What%E2%80%99s%20the%20Difference/IPv4-vs-IPv6.png?width=2750\&name=IPv4-vs-IPv6.png)

### Private and Public IP Addresses

All IPv4 addresses can be divided into two major groups: **global (or public, external)** - this group can also be called 'WAN addresses' — those that are used on the Internet, and **private (or local, internal) addresses** — those that are used in the local network (LAN).

![priv-pub](https://wiki.teltonika-networks.com/wikibase/images/thumb/a/a7/Sip.png/1100px-Sip.png)

### More about **Private IP** addresses:

Private (internal) addresses are not routed on the Internet and no traffic can be sent to them from the Internet, they only supposed to work within the local network. Private addresses include IP addresses from the following subnets:

![private-ip](https://66.media.tumblr.com/02a533c1d55ca0ba83e0176168df06ec/tumblr\_inline\_o4m1taQugo1u4ytoo\_1280.jpg)

### NAT - Network Address Translation

NAT stands for network address translation. It’s a way to map multiple local private addresses to a public one before transferring the information. Organizations that want multiple devices to employ a single IP address use NAT, as do most home routers.

![nat2](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/8275f73b57bdcb982b1d69aa8d213d2bdb384657/nat2.png)

1.  **Static NAT**

    When the local address is converted to a public one, this NAT chooses the same one. This means there will be a consistent public IP address associated with that router or NAT device.
2.  **Dynamic NAT**

    Instead of choosing the same IP address every time, this NAT goes through a pool of public IP addresses. This results in the router or NAT device getting a different address each time the router translates the local address to a public address.

#### ⚠️ IP Addresses operates on **Layer 3 of OSI Model**

_Note: This module will cover OSI model later._

![osi3](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/b9d7f33be654d299f6618feeacb97fc5fd5bd7d2/OSI\_L3.png)

## 3. Subnetting

#### Why subnetting?

The way IP addresses are constructed makes it relatively simple for Internet routers to find the right network to route data into. However, in a Class A network (for instance), there could be millions of connected devices, and it could take some time for the data to find the right device. This is why subnetting comes in handy: subnetting narrows down the IP address to usage within a range of devices.

Because an IP address is limited to indicating the network and the device address, IP addresses cannot be used to indicate which subnet an IP packet should go to. Routers within a network use something called a subnet mask to sort data into subnetworks.

> ⚠️ Subnetting is really important for penetration testers and aspiring hackers, eventually you will face several cases involving small or large networks in your future engagements. Understanding the IP address type, range, available hosts is crucial for any network analysis.

### Cheat sheet makes easier for subnetting

![subnetting](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/5ce4b7daa9c2c10ccd44675eadaceae646e487e2/cyber-mentor-subnetting.png)

* CyberMentor Subnetting Sheet: https://twitter.com/thecybermentor/status/1211335431406727169
* Subnetting Cheat sheet alternative: https://nsrc.org/workshops/2009/summer/presentations/day3/subnetting.pdf

### Exercises:

Subnetting comes in handy to awnser basic questions like:

* Identify the network and broadcast address
* How many hosts available in the network/hosts range?
* What masks allow the particular host?

| IP range        | Subnet          | Hosts | Network      | Broadcast    |
| --------------- | --------------- | ----- | ------------ | ------------ |
| 192.168.1.16/28 | 255.255.255.240 | 14    | 192.168.1.16 | 192.168.1.31 |
| 192.168.0.0/22  | ?               | ?     | ?            | ?            |

* Take the `192.168.0.0/22` IP range listed above
* You can easily figure out the subnet mask by look the cheat sheet, you can see the `252` column. Just replace the value of `x`. You will get `255.255.252.0`
  * Subnet masks can be 0, 128, 192, 224, 240, 248, 252, 254 and 255.
  * To understand the basics of math behind the bits, check the next figure below:

![bits](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/c1e01e29aedc394f2d75c4ccf57e72606775103a/bits.png)

* The number of hosts is `2^(n) - 2`.
  * `n = off bits`
  * In this case, is 2^10 = 1024 -> 1024 - 2 = `1022`
* The network portion is the first and lowest possible value.
* The broadcast is the last and highest possible value.

| IP range       | Subnet        | Hosts | Network     | Broadcast     |
| -------------- | ------------- | ----- | ----------- | ------------- |
| 192.168.0.0/22 | 255.255.252.0 | 1022  | 192.168.0.0 | 192.168.3.255 |

### Other relevant information about IPs

* **IPv4 Main Address Types**
  * **Unicast** - acted on by a single recipient
  * **Multicast** - acted on by members of a specific group
  * **Broadcast** - acted on by everyone on the network
    * **Limited** - delivered to every system in the domain (255.255.255.255)
    * **Directed** - delivered to all devices on a subnet and use that broadcast address
* **Subnet mask** - determines how many address available on a specific subnet
  * Represented by three methods
    * **Decimal** - 255.240.0.0
    * **Binary** - 11111111.11110000.00000000.00000000
    * **CIDR** - x.x.x.x/12 (where x.x.x.x is an ip address on that range)
  * If all the bits in the host field are 1s, the address is the broadcast
  * If they are all 0s, it's the network address
  * Any other combination indicates an address in the range

## MAC Addresses

* MAC (Media Access Control) address is provided by NIC Card'd manufacturer and gives the physical address of a computer.

![macphys](https://i1.wp.com/learntomato.flashrouters.com/wp-content/uploads/MAC-address-hardware.jpg?resize=560%2C315\&ssl=1)

The first three bytes of a MAC address were originally known as **OUI’s, or Organizational Unique Identifiers. Each manufacturer of networking equipment was assigned an OUI, and was free to assign their own numbers in that block.**

```
   OUI     NIC
    |       |
________ ________
00:0c:29:99:98:ca
```

### Checking vendor behind MAC addresse

1. Check your MAC address use the command `ifconfig` (Linux) or `/ipconfig` (Windows) ![mac](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/214242916f8947f09fc15d5bdde6a668fd4a4c1f/mac2.png)
2. Copy and save the **first three bytes** of your address. _(The first three bytes from image above is `00:0c:29`)_
3. Validate the information by performing a **MAC Address Lookup** on the internet. For this example I'm using: https://aruljohn.com/ ![mac2](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/c82686452d3e671f9a4d351cd5c02171914dd16d/mac2lookup.png)
4. As you can see the OUI lookup identify a virtual network interface provided by VMware

_So, to summarize, the **first three bytes** are assigned to a manufacturer of networking equipment and the manufacturer assigns the last three bytes of an address._

#### ⚠️ MAC Addresses operates on Layer 2 of OSI Model

![osil2](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/b9d7f33be654d299f6618feeacb97fc5fd5bd7d2/OSI\_L2.png)

## 4. TCP/IP, UDP and 3-Way-Handshake

### Transmission Control Protocol/Internet Protocol (TCP/IP)

* What is TCP used for?

TCP enables data to be transferred between applications and devices on a network. It is designed to break down a message, such as an email, into packets of data to ensure the message reaches its destination successfully and as quickly as possible.

* What does TCP mean?

TCP means Transmission Control Protocol, which is a communications standard for delivering data and messages through networks. TCP is a basic standard that defines the rules of the internet and is a common protocol used to deliver data in digital network communications.

* The TCP/IP model consists of several types of protocols, including:
  * TCP and IP
  * Address Resolution Protocol (ARP)
  * Internet Control Message Protocol (ICMP)
  * Reverse Address Resolution Protocol (RARP)
  * User Datagram Protocol (UDP)

![tcpmod](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/bccff9a7c15aa11636c03686ef344ae2d433f699/tcpmodel.png)

TCP/IP Model

TCP is the most commonly used of these protocols and accounts for the most traffic used on a TCP/IP network. **UDP is an alternative to TCP that does not provide error correction, is less reliable, and has less overhead, which makes it ideal for streaming.**

### The User Datagram Protocol (UDP)

Is a lightweight data transport protocol that works on top of IP. UDP provides a mechanism to detect corrupt data in packets, but it does not attempt to solve other problems that arise with packets, such as lost or out of order packets. That's why UDP is sometimes known as the Unreliable Data Protocol. UDP is simple but fast, at least in comparison to other protocols that work over IP. It's often used for time-sensitive applications (such as real-time video streaming) where speed is more important than accuracy.

* On Linux and Unix systems you can issue the `lsof` command to see which processes is using UDP ports ![udp](https://cdn.kastatic.org/ka-perseus-images/edbdf593300fc4a51c60a97998c4d01a51ccd3b1.png)

### The TCP format

![tc](https://cdn.kastatic.org/ka-perseus-images/e5fdf560fdb40a1c0b3c3ce96f570e5f00fff161.svg)

### The UDP format

![udp](https://cdn.kastatic.org/ka-perseus-images/9d185d3d44c7ef1e2cd61655e47befb4d383e907.svg)

### TCP Handshake

TCP uses a three-way handshake to establish a reliable connection. The connection is full duplex, and both sides synchronize (SYN) and acknowledge (ACK) each other. The exchange of these four flags is performed in three steps:

1. SYN
2. SYN-ACK
3. ACK

![3wayhandshake](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/bd38a6a2d83ea02a4715d6cb7fd8e0d74af3bd26/3wayhs.jpg)

The three message mechanism is designed so that two computers that want to pass information back and forth to each other can negotiate the parameters of the connection before transmitting data such as HTTP browser requests.

### More TCP Flags

| Flag | Name           | Function                                                                         |
| ---- | -------------- | -------------------------------------------------------------------------------- |
| SYN  | Synchronize    | Set during initial communication. Negotiating of parameters and sequence numbers |
| ACK  | Acknowledgment | Set as an acknowledgement to the SYN flag. Always set after initial SYN          |
| RST  | Reset          | Forces the termination of a connection (in both directions)                      |
| FIN  | Finish         | Ordered close to communications                                                  |
| PSH  | Push           | Forces the delivery of data without concern for buffering                        |
| URG  | Urgent         | Data inside is being sent out of band. Example is cancelling a message           |

### Capturing 3 Way handshakes (Example)

* The figure below shows the 3-way-handshake packets captured by [Wireshark](https://www.wireshark.org/)

![wireshark](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/5213becc28e3f9f46c976d05cd090ffd070ff5d1/wireshark0.png)

## 5. Ports & Protocols

### What is a Port?

In computer networking, a port is a communication endpoint. At the software level, within an operating system, a port is a logical construct that identifies a specific process or a type of network service.

### The most common ports

As a penetration tester or ethical hacker you should be familiar with the common ports and protocols used by popular services.

#### Port Numbers

* **Internet Assigned Numbers Authority** (IANA) - maintains Service Name and Transport Protocol Port Number Registry which lists all port number reservations
* Ranges
  * **Well-known ports** - 0 - 1023
  * **Registered ports** - 1024 - 49,151
  *   **Dynamic ports** - 49,152 - 65,535

      | Port Number | Protocol | Transport Protocol |
      | ----------- | -------- | ------------------ |
      | 20/21       | FTP      | TCP                |
      | 22          | SSH      | TCP                |
      | 23          | Telnet   | TCP                |
      | 25          | SMTP     | TCP                |
      | 53          | DNS      | TCP/UDP            |
      | 67          | DHCP     | UDP                |
      | 69          | TFTP     | UDP                |
      | 80          | HTTP     | TCP                |
      | 110         | POP3     | TCP                |
      | 135         | RPC      | TCP                |
      | 137-139     | NetBIOS  | TCP/UDP            |
      | 143         | IMAP     | TCP                |
      | 161/162     | SNMP     | UDP                |
      | 389         | LDAP     | TCP/UDP            |
      | 443         | HTTPS    | TCP                |
      | 445         | SMB      | TCP                |
      | 514         | SYSLOG   | UDP                |
  * A service is said to be **listening** for a port when it has that specific port open
  * Once a service has made a connection, the port is in an **established** state
  * **`netstat`** command:
    * Shows open ports on computer
    * **netstat -an** displays connections in numerical form
    * **netstat -b** displays executables tied to the open port (admin only)

## 6. OSI Model

OSI Model is a hypothetical networking framework that uses specific protocols and mechanisms in every layer of it. This model is used to divide the network architecture into seven different layers conceptually. These layers are:

![osi-model](https://gist.githubusercontent.com/Samsar4/62886aac358c3d484a0ec17e8eb11266/raw/3e2dc59e7c341f4d79b2b93bac03fd8378c7ae3a/tcpmo.jpg)

There also involves some security postures and mechanisms that a security professional must know to detect and put the security method effectively in every layer.

### More about the Layers:

### Layer 7 - Application

![l7](https://www.cloudflare.com/img/learning/ddos/glossary/open-systems-interconnection-model-osi/7-application-layer.svg)

* This is the only layer that directly interacts with data from the user. Software applications like web browsers and email clients rely on the application layer to initiate communications. But it should be made clear that client software applications are not part of the application layer; rather the application layer is responsible for the protocols and data manipulation that the software relies on to present meaningful data to the user. Application layer protocols include HTTP as well as SMTP (Simple Mail Transfer Protocol is one of the protocols that enables email communications).

### Layer 6 - Presentation

![l6](https://www.cloudflare.com/img/learning/ddos/glossary/open-systems-interconnection-model-osi/6-presentation-layer.svg)

* This layer is primarily responsible for preparing data so that it can be used by the application layer; in other words, layer 6 makes the data presentable for applications to consume. The presentation layer is responsible for translation, encryption, and compression of data.

### Layer 5 - Session Layer

![l5](https://www.cloudflare.com/img/learning/ddos/glossary/open-systems-interconnection-model-osi/5-session-layer.svg)

* This is the layer responsible for opening and closing communication between the two devices. The time between when the communication is opened and closed is known as the session. The session layer ensures that the session stays open long enough to transfer all the data being exchanged, and then promptly closes the session in order to avoid wasting resources.

### Layer 4 - Transport Layer

![l4](https://www.cloudflare.com/img/learning/ddos/glossary/open-systems-interconnection-model-osi/4-transport-layer.svg)

* Layer 4 is responsible for end-to-end communication between the two devices. This includes taking data from the session layer and breaking it up into chunks called segments before sending it to layer 3. The transport layer on the receiving device is responsible for reassembling the segments into data the session layer can consume.
* The transport layer is also responsible for flow control and error control. Flow control determines an optimal speed of transmission to ensure that a sender with a fast connection doesn’t overwhelm a receiver with a slow connection. The transport layer performs error control on the receiving end by ensuring that the data received is complete, and requesting a retransmission if it isn’t.

### Layer 3 - Network Layer

![l3](https://www.cloudflare.com/img/learning/ddos/glossary/open-systems-interconnection-model-osi/3-network-layer.svg)

* The network layer is responsible for facilitating data transfer between two different networks. If the two devices communicating are on the same network, then the network layer is unnecessary. The network layer breaks up segments from the transport layer into smaller units, called packets, on the sender’s device, and reassembling these packets on the receiving device. The network layer also finds the best physical path for the data to reach its destination; this is known as routing.

### Layer 2 - Data Link Layer

![l2](https://www.cloudflare.com/img/learning/ddos/glossary/open-systems-interconnection-model-osi/2-data-link-layer.svg)

* The data link layer is very similar to the network layer, except the data link layer facilitates data transfer between two devices on the SAME network. The data link layer takes packets from the network layer and breaks them into smaller pieces called frames. Like the network layer, the data link layer is also responsible for flow control and error control in intra-network communication (The transport layer only does flow control and error control for inter-network communications).

### Layer 1 - Physical Layer

![l1](https://www.cloudflare.com/img/learning/ddos/glossary/open-systems-interconnection-model-osi/1-physical-layer.svg)

* This layer includes the physical equipment involved in the data transfer, such as the cables and switches. This is also the layer where the data gets converted into a bit stream, which is a string of 1s and 0s. The physical layer of both devices must also agree on a signal convention so that the 1s can be distinguished from the 0s on both devices.
