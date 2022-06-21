**Name:** CCTV

**Challenge:** REV

**IP:** 34.149.14.242

**Date:** 21/06/2022

**Web-Technology:**
- JavaScript
- XMPP
- Mcafee ePO

================================================================

**TO-DO LIST:**
___
* Initial Enumeration
* Port Scan
* Check Source Code
* Research Methods
* Create Script
* Exploit

================================================================

**NMAP:**
___

```sh
PORT      STATE SERVICE    REASON  VERSION  
1/tcp     open  tcpwrapped syn-ack  
25/tcp    open  tcpwrapped syn-ack  
|_smtp-commands: Couldnt establish connection on port 25  
43/tcp    open  tcpwrapped syn-ack  
80/tcp    open  http       syn-ack lighttpd 1.4.55  
| http-methods:    
|_  Supported Methods: OPTIONS GET HEAD POST  
|_http-title: CCTV  
|_http-server-header: lighttpd/1.4.55  
83/tcp    open  tcpwrapped syn-ack  
85/tcp    open  tcpwrapped syn-ack  
89/tcp    open  tcpwrapped syn-ack  
110/tcp   open  tcpwrapped syn-ack  
143/tcp   open  tcpwrapped syn-ack  
443/tcp   open  ssl/http   syn-ack lighttpd 1.4.55  
<--SNIP-->
465/tcp   open  tcpwrapped syn-ack  
|_smtp-commands: Couldnt establish connection on port 465  
587/tcp   open  tcpwrapped syn-ack  
|_smtp-commands: Couldnt establish connection on port 587  
700/tcp   open  tcpwrapped syn-ack  
993/tcp   open  tcpwrapped syn-ack  
995/tcp   open  tcpwrapped syn-ack  
1443/tcp  open  tcpwrapped syn-ack  
1688/tcp  open  tcpwrapped syn-ack  
2022/tcp  open  tcpwrapped syn-ack  
3269/tcp  open  tcpwrapped syn-ack  
3306/tcp  open  tcpwrapped syn-ack  
|_ssl-date: ERROR: Script execution failed (use -d to debug)  
|_ssl-cert: ERROR: Script execution failed (use -d to debug)  
|_mysql-info: ERROR: Script execution failed (use -d to debug)  
|_sslv2: ERROR: Script execution failed (use -d to debug)  
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)  
|_tls-alpn: ERROR: Script execution failed (use -d to debug)  
3389/tcp  open  tcpwrapped syn-ack  
5225/tcp  open  tcpwrapped syn-ack  
5432/tcp  open  tcpwrapped syn-ack  
5900/tcp  open  tcpwrapped syn-ack  
8022/tcp  open  tcpwrapped syn-ack  
8080/tcp  open  http-proxy syn-ack  
<--SNIP-->
8086/tcp  open  tcpwrapped syn-ack  
8088/tcp  open  tcpwrapped syn-ack  
8090/tcp  open  tcpwrapped syn-ack  
8099/tcp  open  tcpwrapped syn-ack  
9200/tcp  open  tcpwrapped syn-ack  
15004/tcp open  tcpwrapped syn-ack  
30000/tcp open  tcpwrapped syn-ack
```

So many open ports..

================================================================

**WEB RESULTS:**
___

[+] `MANUAL:`

CTRL + U brings up the page source:
There's a JavaScript with a password function. The code seems to convert Clear Text to ASCII then compare it to the if statement. It uses `0xCafe` ([Link](https://www.hexadecimaldictionary.com/hexadecimal/0xCAFE/)) to convert the characters.

```JS
    <script>
    const checkPassword = () => {
      const v = document.getElementById("password").value; 
      const p = Array.from(v).map(a => 0xCafe + a.charCodeAt(0));
    
      if(p[0] === 52037 &&
         p[6] === 52081 &&
         p[5] === 52063 &&
         p[1] === 52077 &&
         p[9] === 52077 &&
         p[10] === 52080 &&
         p[4] === 52046 &&
         p[3] === 52066 &&
         p[8] === 52085 &&
         p[7] === 52081 &&
         p[2] === 52077 &&
         p[11] === 52066) {
        window.location.replace(v + ".html");
      } else {
        alert("Wrong password!");
      }
    }
    
    window.addEventListener("DOMContentLoaded", () => {
      document.getElementById("go").addEventListener("click", checkPassword);
      document.getElementById("password").addEventListener("keydown", e => {
        if (e.keyCode === 13) {
          checkPassword();
        }
      });
    }, false);
    </script>
```

================================================================

**OTHER ENUM:**
___

Tried using scripts to exploit ports `5222` XMPP and `8081` Mcafee ePO but neither worked

================================================================

**EXPLOITATION:**
___
```python

# Using the character set that was provided - The numbers on the left correlate to an ASCII letter, the right are 0xCafe converted ASCII
code = {

    0: 52037,
    6: 52081,
    5: 52063,
    1: 52077,
    9: 52077,
    10: 52080,
    4: 52046,
    3: 52066,
    8: 52085,
    7: 52081,
    2: 52077,
    11: 52066,

}

# Make password variable
password = ""

# Loop code and decode using 0xCafe
for i in range (max(code.keys()) + 1):
	password += chr(code[i] - 0xCafe) #Take the code, subtract by the 0xCafe code

# Print out the password
print (password)
```

