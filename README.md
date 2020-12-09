# password-manager
Python/SQL Password Manager

Inspired by [Kalle Hallden's pwManager](https://github.com/KalleHallden/pwManager) and other similar projects.

Objective: Build a password manager that can be run from the command line (Why? I wanted a password manager I could use to generate and save hashed passwords, without relying on Safari/Chrome.)

Version 0.1:
- Working password manager leveraging the passlib hashing library.
- Password details (website and username) are saved and stored to a python dictionary in a pickle file.
- Passwords can be retrieved by providing the same master password, website and username to the app.

Notes: pw_secret.py contains functions to retrieve the unique hashing salt and app password and has been left out of the repository.

Features to add(?):
- To store passwords in SQLite database
- Custom password lengths + requirements
