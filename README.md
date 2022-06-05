The rapid development of the Internet has increased the importance of various utilities such as password managers. While not everyone can trust third party programs, I have built a small Python program that has three entries (website name, username and password). The program can save your login and password from different websites in a separate file (passwords_data.py), and if desired, the program can generate a random password from 8 to 16 characters long.

Functionality:
- "Find" button: Finds and displays all logins/passwords from the website entered in the "Websites" field. If you have more than 1 login for this website, when you click the ""Find" button again, the program will display the next account. At the end of the list of logins / passwords, the program will re-show logins / passwords starting from the first one.
- Generate: Generates a new random password (8 to 16 characters). You can change it or write your own password.
- Add/Edit: Saves changes made to the program. Thus, after opening the program the next time, the entered data will not be lost.
- Clear: Removes all information from all fields (Website, login and password) to facilitate the introduction of new data.

The application was written in Python 3 using the Tkinter library. 
