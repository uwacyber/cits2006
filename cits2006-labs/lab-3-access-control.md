# Lab 3: Access Control

## 3.1. Introduction
Access control has two fundamental components: authentication and authorization. Authentication is the process of verifying the identity of a user, process, or device. Authorization is the process of determining whether a user, process, or device is allowed to access a resource. In this lab, we will explore these concepts in more detail.

## 3.2. Authentication
Authentication is the process of verifying the identity of a user, process, or device. There are three primary methods of authentication: something you know, something you have, and something you are. These are often referred to as knowledge factors, possession factors, and inherence factors, respectively. In this lab, we'll try to implement some of these concepts, but due to physical limitations (i.e., only have access from your computer), some concepts like biometrics and tokens will not be covered. However, you'll have sufficient understanding to be able to implement them, if you need to.

### 3.2.1. Passwords
Passwords are the most common form of authentication. They are a knowledge factor, meaning that they are something you know. In this section, we will explore the use of passwords for authentication.

We'll start with the most simplest implementation, then add features to make it more secure. Download the template code for this section:

```
curl -LO https://github.com/uwacyber/cits2006/raw/live/cits2006-labs/files/password.py
```

Run this code to check that it is working correctly (i.e., with the right username and password, you can authenticate yourself). The starter now rejects unknown usernames and limits attempts to three. Earlier versions printed "Authenticated!" for any unknown username. Can you see why?

```text
$ python3 password.py
Enter Your Username : user1
Enter Your Password :
Authenticated!
```

(The password you type is not shown.)

However, this is not secure at all. The password is stored in plaintext, and anyone who has access to the file can see the password. We will now add some security features to make it more secure.

### 3.2.2. Salting and Hashing
To make the password more secure, we will use a technique called salting and hashing. You should remember about hashing from Lab 1. Salting is the process of adding a random value to the password before hashing it. This makes it more difficult for an attacker to use a precomputed table of hashes (a rainbow table) to crack the password. Hashing is the process of converting the password into a fixed-length string of characters. This makes it difficult for an attacker to determine the original password from the hash.

We will use the `bcrypt` library to hash the password. Install this library if you haven't done already. This library automatically generates a random salt and hashes the password. bcrypt works on bytes, so convert strings with `.encode()` (e.g., `password.encode()`) before hashing or checking.

```python
database = {"user1": "123456", "user2": "654321"}
new_database = {}
for user, password in database.items():
    new_database[user] = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
```

The above code will convert the original database dictionary of plaintext to a new dictionary of hashed passwords. You can then use this new dictionary to authenticate users now. Checking the password using the `bcrypt` library is simple:

```python
bcrypt.checkpw(password.encode(), hashed_password)
```

#### TASK 1
Edit `password.py` so that `database` holds bcrypt hashes instead of plaintext passwords, and `check()` verifies the password against the stored hash. The program should behave as before: the right username and password authenticate, wrong passwords do not, and unknown usernames are still rejected.


Note that, when checking the password you don't need to provide the salt to the checker, because the salt is stored in the hashed password. The `bcrypt` library will automatically extract the salt from the hashed password and use it to check the password. However, if you are implementing your own library or using other libraries, you may need to store the salt separately and provide it to the checker.




### 3.2.3. Time-based One-time Passwords (TOTP)
Time-based One-time Passwords (TOTP) are a form of two-factor authentication. They are a possession factor, meaning that they are something you have. TOTP works by generating a one-time password based on a shared secret and the current time. The shared secret is usually delivered as a QR code (encoding an `otpauth://` URI) that is scanned into an authenticator app, such as Google Authenticator. The authenticator app then generates a one-time password based on the shared secret and the current time. The server can then verify the one-time password by generating the same one-time password based on the shared secret and the current time and comparing it to the one-time password provided by the user.

You can start with the basic template provided below:

```
curl -LO https://github.com/uwacyber/cits2006/raw/live/cits2006-labs/files/totp_mfa.py
```

The code is not quite complete, you will have to complete the `verify_totp` function to make it work properly (currently it will authenticate any code!). But first, let's look at the rest of the functions provided to you.

The code follows the standards, so it works with real authenticator apps (Google Authenticator, Microsoft Authenticator, 1Password and others).

- `hotp()` implements RFC 4226. It decodes the base32 secret, computes HMAC-SHA1 over an 8-byte counter, then uses *dynamic truncation*: the low 4 bits of the last byte choose where to take 4 bytes from, and the top bit is masked off. The result modulo 10^6 is the 6-digit code.
- `totp()` implements **RFC 6238**: it is HOTP with the counter set to the current Unix time divided by **30 seconds**.

Run the script, add the printed key to an authenticator app on your phone, and check that the codes match. It will look something like below (your key and code will differ, and the code changes every 30 seconds):

```text
$ python3 totp_mfa.py
Add this account to an authenticator app (enter the key manually):
  key: E6KAMIM6EXUESTC2FVINWUPV64NRGJCT
  or URI: otpauth://totp/CITS2006:lab3?secret=E6KAMIM6EXUESTC2FVINWUPV64NRGJCT&issuer=CITS2006
Current code from this script: 472771
Enter the code shown in your authenticator app:
```

#### TASK 2
Complete `verify_totp()`. Accept the code for the current 30-second step, or for up to `window` steps either side (default 1, i.e. ±30 seconds, for clock drift and typing time). Compare with `hmac.compare_digest`. **Extension:** a code should only work once. Add a record of used (secret, step) pairs and reject replays.



## 3.3. Linux ACLs
Access Control Lists (ACLs) are a way to define more fine-grained access control than the traditional Unix file permissions. In this section, we will explore how to use ACLs to control access to files and directories in the Linux environment. Please note, if you are not familiar with permissions in Linux, please revisit lab 0. To do this section, you will need an access to a Linux environment (use the Lab 0 container: `docker run --rm -it cits2006-env`, where you have sudo). In the container you are the user `student`. Do not mount a folder from your laptop with `-v` for this section: file ownership and ACL changes do not work reliably on mounted folders.

The output below was produced in that container. Your dates will differ, and the user and group IDs may differ if you create users in a different order.


### 3.3.1. Setting up the environment
We will start by creating a folder to keep files for sales department. We will work in `/tmp/acl`, because other users (created below) must be able to reach the folder: your home folder is private to you, and `/work` belongs to root.

```text
$ mkdir /tmp/acl && cd /tmp/acl
$ mkdir sales
$ ls -al
total 12
drwxr-xr-x 3 student student 4096 Oct  6 08:18 .
drwxrwxrwt 1 root    root    4096 Oct  6 08:18 ..
drwxr-xr-x 2 student student 4096 Oct  6 08:18 sales
```

We can easily check the current ACL associated with this folder by using the `getfacl` command. The output will be similar to the following:

```text
$ getfacl sales
# file: sales
# owner: student
# group: student
user::rwx
group::r-x
other::r-x
```

#### TASK 3
Obviously, we don't want to own this folder ourselves (assuming you are using your own account and created the folder as above), as well as to give everyone access to this folder. We will (1) create a new group called `sales` and a new user called `salesuser`, and give the ownership of the folder to this user and group, and (2) give the owner and the group full access (`rwx`) and remove all permissions for `other`. 

{% hint style="hint" %}
If this isn't familiar, please revise Lab 0!
{% endhint %}

Once complete, it should look as below:

```text
$ ls -al
total 12
drwxr-xr-x 3 student   student 4096 Oct  6 08:18 .
drwxrwxrwt 1 root      root    4096 Oct  6 08:18 ..
drwxrwx--- 2 salesuser sales   4096 Oct  6 08:18 sales
$ getfacl sales
# file: sales
# owner: salesuser
# group: sales
user::rwx
group::rwx
other::---
```


### 3.3.2. Using ACLs
Let's try and create a file inside the `sales` directory. Using your current account (which should not be in the `sales` group), try to create a file inside the `sales` directory. You will notice that you are not able to do so. This is because you don't have the permission to do so. We will now use ACLs to give you the permission to create files inside the `sales` directory.

This is done by adjusting the permission of the user using the `setfacl` command. The command to give the user permission to create files inside the `sales` directory is as follows:

```bash
sudo setfacl -m u:your_username:rwx sales
```

Replace `your_username` with your username (in the container, `student`). You need `sudo` because only the owner of `sales` (now `salesuser`, not you) or root can change its ACL. After running this command, you should be able to create files inside the `sales` directory.

```text
$ cd sales
bash: cd: sales: Permission denied
$ setfacl -m u:student:rwx sales
setfacl: sales: Operation not permitted
$ sudo setfacl -m u:student:rwx sales
$ cd sales
$ cd ..
```

The commands in the rest of this lab are run from `/tmp/acl`.

At this stage, create a couple of files inside the `sales` directory (for example, `echo "hello world" > sales/test.txt`). We will use these files for later tasks.

Next, we will create a user `john`, and give him the permission to ONLY read the files inside the `sales` directory.

#### TASK 4
Create a user `john` and give him the permission to read the files inside the `sales` directory. To act as John, run a command with `sudo -u john` (for example, `sudo -u john ls sales`). Once complete, you should be able to check as below.

```text
$ groups john
john : sales
$ id john
uid=1002(john) gid=1001(sales) groups=1001(sales)
$ sudo -u john ls sales
test.txt
$ sudo -u john cat sales/test.txt
hello world
$ sudo -u john touch sales/test2.txt
touch: cannot touch 'sales/test2.txt': Permission denied
```

John is a member of `sales`, and the `sales` group has `rwx` on the folder, yet John cannot create files there. Why? (Hint: the order in which ACL entries are checked is described in the [acl(5) manual page](https://man7.org/linux/man-pages/man5/acl.5.html); the container has no `man` command.)

Because John cannot create files directly inside the `sales` directory, we will create a subdirectory called `john` inside the `sales` directory, and give John the permission to create files inside this subdirectory. If done correctly, you can see the permission as below.

```text
$ ls -al sales
total 16
drwxrwx---+ 3 salesuser sales   4096 Oct  6 08:18 .
drwxr-xr-x  3 student   student 4096 Oct  6 08:18 ..
drwxr-xr-x  2 john      sales   4096 Oct  6 08:18 john
-rw-r--r--  1 student   student   12 Oct  6 08:18 test.txt
$ sudo -u john touch sales/john/test2.txt
$ ls -al sales/john
total 8
drwxr-xr-x  2 john      sales 4096 Oct  6 08:18 .
drwxrwx---+ 3 salesuser sales 4096 Oct  6 08:18 ..
-rw-r--r--  1 john      sales    0 Oct  6 08:18 test2.txt
```

Since his folder belongs to the `sales` group, other members of the `sales` group can also access his folder (e.g., list the files there). We may want to keep this directory private to John only. This can be achieved by removing permissions for specific users or groups. First, create another member of the sales team, David, and remove his access to John's directory:

```bash
sudo useradd -m david && sudo usermod -aG sales david
sudo setfacl -m u:david:- sales/john
```

The `setfacl` command adds an entry for David with no permissions, so he is disallowed from accessing John's directory, even though he is a member of `sales`. You should try and check that this is working as intended. When you have done it, you should observe the same behaviour as below: David is refused, while another member of `sales` is not.

```text
$ sudo setfacl -m u:david:- sales/john
$ sudo -u david ls sales/john
ls: cannot open directory 'sales/john': Permission denied
$ sudo -u salesuser ls sales/john
test2.txt
```

Next, we remove the access of the rest of the `sales` group and of everyone else:

```bash
sudo setfacl -m g::-,o::- sales/john
```

`g::` is the entry for the directory's owning group (here, `sales`) and `o::` is `other`. Why not `g:sales:-`? Because `sales` is already the owning group, so the `group::` entry would still let its members in: a user is allowed when any group entry that applies to them grants the access. Check that John's directory is now private to John, as below.

```text
$ sudo setfacl -m g::-,o::- sales/john
$ sudo -u salesuser ls sales/john
ls: cannot open directory 'sales/john': Permission denied
$ sudo -u john ls sales/john
test2.txt
$ getfacl sales/john
# file: sales/john
# owner: john
# group: sales
user::rwx
user:david:---
group::---
mask::---
other::---
```


You still would like to give certain users permission to access John's directory (e.g., you are the boss and you want to access his directory). You can do this by adding the permission to the specific user or group.

```bash
sudo setfacl -m u:your_username:rwx sales/john
```

Now, you are once again able to access John's directory. You should have the same behaviour as follows.

```text
$ touch sales/john/hello.txt
touch: cannot touch 'sales/john/hello.txt': Permission denied
$ sudo setfacl -m u:student:rwx sales/john
$ touch sales/john/hello.txt
$ getfacl sales/john
# file: sales/john
# owner: john
# group: sales
user::rwx
user:student:rwx
user:david:---
group::---
mask::rwx
other::---
```


This covers the basics of using ACLs, now you can create and control access in Linux for various users. However, you would be able to see that this can become quite complex and difficult to manage. There are other concepts and methods, such as chroot, that can be used to control access in Linux. The concept of ACL isn't limited to Linux, it is also used in Windows and other operating systems. For example, Windows uses NTFS ACLs to control access to files and directories (Active Directory is the directory service that manages the users and groups those ACLs refer to).

## 3.4 Summary

In this lab, we looked at some fundamental controls used in access control. Obviously, we have more comprehensive suite of access control mechanisms used in practice, but these are the founding blocks of setting up access control. 

Next up, protocols and tools.
