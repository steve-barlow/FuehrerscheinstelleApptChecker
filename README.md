FuehrerscheinstelleApptChecker
==============================

Check every 5 minutes if there is any change on the stadt.muenchen.de page to book an appointment to transfer
a foreign driver's licence and alert if there is, meaning an appointment might be available.

Written for Apple Mac.

Installation
------------

* To set up virtual environment first time - from this directory:  
   ```
   % python -m venv venv
   % source venv/bin/activate
   % python -m pip install --upgrade pip
   % pip install -r requirements.txt
   ```

* To use virtual environment, not first time - from this directory:  
   ```
   % source venv/bin/activate
   ```

Example
-------

```
(venv) % ./FuehrerscheinstelleApptChecker.py
Doing initial read
Now polling every 5 minutes
2023-02-10 23:18:27 : Unchanged
2023-02-10 23:23:34 : Unchanged
2023-02-10 23:28:41 : Unchanged
2023-02-10 23:33:48 : Unchanged
2023-02-10 23:38:55 : Unchanged
2023-02-10 23:44:02 : Unchanged
2023-02-10 23:49:09 : Unchanged
2023-02-10 23:54:16 : Unchanged
2023-02-10 23:59:23 : Unchanged
2023-02-11 00:04:31 : Appointments updated
Manually make appointment in browser window. Press return to exit.
(venv) %
```

Useful Websites
---------------

* https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_fs.html?&loc=FS&ct=1071898
* https://selenium-python.readthedocs.io/
