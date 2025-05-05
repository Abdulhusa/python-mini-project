# Python Password Manager

## Project Documentation

### Overview
The Python Password Manager is a secure, command-line based application that allows users to store, retrieve, update, and delete their passwords. The application uses SQLite as the database backend for persistent storage of passwords.

<p align="center">
  <img src="https://cyberpedia.reasonlabs.com/IMG/password%20generator.jpg" alt="Password Generator" width="510"/>
</p>

### Project Structure

├── main.py                # Main application entry point <br/>
├── passwords.db           # SQLite database file<br/>
├── sqlite3_handler.py     # Database operations handler<br/>
└── __pycache__/           # Python cache directory<br/>

### Features
- **Password Storage**: Store website/service names with associated usernames and passwords
- **Password Retrieval**: Quickly access stored passwords
- **Password Generation**: Generate strong random passwords
- **Password Updates**: Modify existing password entries
- **Password Deletion**: Remove unwanted entries
- **Local Storage**: All data is stored locally on your machine

### Technical Details

#### Dependencies
- Python 3.6+
- SQLite3 (included in Python's standard library)

#### Database Schema
The `passwords.db` SQLite database contains a table structure that typically includes:
- Website/Service name
- Username/Email
- Password
- Date

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
