
#### Author name
Charles Schiedel

# PASSWORD LOCKER
This is a Python app that allows the user to save his or her passwords to their various accounts. The app can also generate random unique passwords for the user.

## Description
This is an app that allows users to store account credentials, create new accounts and store their credentials, they can also delete those credentials.

## Technologies Used
Python 3.6

## Installation requirements
Ensure you have Python3.6 installed in your computer. you can download it by running this command
$ sudo apt-get update sudo apt-get install python3.6.

Ensure you have PiP installed in your computer, you can download it by running this command:
$ python get-pip.py

From the repository, click + in the global sidebar and select Clone this repository .

Copy the clone command.

Run the following command to make the app executable;

$ chmod +x run.py

Run this command to open the app
$ ./run.py


## BDD
| Behaviour        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Short codes display | User keys in `li` | Input fields for the names and password appear |
| Input fields accept input | User adds his/her name and password | Password locker account is created |
| Other short codes appear | User keys in `ca` | User enters account name and username |
| Options for password input display | User enters `ep` | User can input preferred password |
| Options for password input display | User keys in `gp` | An 8 character password is generated automatically |
| Short codes reappear | User keys in `da` | The accounts are displayed by the name,username and password |
| Short codes displayed | User keys in`lo` | The user logs out of his/her password locker account |
| Initial short codes appear | User keys in `ex` | User exits the application |

## Technologies used

Technologies used to write the application are:
- Python

## Known bugs and malfunctions
There are no known bugs.If found please contact the developer through [email](https://www.gmail.com).

#### License and copyright information



Copyright (c) 2019 Charles Schiedel
