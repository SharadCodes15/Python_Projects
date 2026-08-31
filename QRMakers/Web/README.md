🗄️ Sample SQLite Database

A lightweight Python project that automatically creates and populates a sample SQLite database for development, testing, and learning.

✨ Features
🐍 Built with Python
🗄️ Uses the built-in SQLite3 database engine
📦 No external dependencies
👤 Includes a sample users table
🌱 Automatically inserts sample data
🔄 Safe to run multiple times without creating duplicate users
📁 Project Structure
sample-database/
│
├── 🐍 app.py
├── 🗄️ database.db
└── 📖 README.md


Note: database.db is generated automatically when you run the application.

🚀 Getting Started
1. Clone or download the project

Navigate to the project directory:

cd sample-database

2. Run the application
python app.py


If your system uses python3:

python3 app.py

3. 🎉 Done!

You should see:

Database created successfully: database.db


A new database.db file will now appear in your project directory.

🗃️ Database Schema

The application creates a users table:

Column	Type	Description
id	INTEGER	Unique user ID
name	TEXT	User's name
email	TEXT	User's email address
age	INTEGER	User's age
Example
users
├── id
├── name
├── email
└── age

👥 Sample Data

The database comes with a few example users:

ID	Name	Email	Age
1	Alice	alice@example.com	25
2	Bob	bob@example.com	30
3	Charlie	charlie@example.com	28
🔧 How It Works

app.py performs the following steps:

Start
  │
  ▼
Connect to SQLite
  │
  ▼
Create users table
  │
  ▼
Insert sample users
  │
  ▼
Commit changes
  │
  ▼
Create database.db
  │
  ▼
Done 🎉


The script uses Python's built-in sqlite3 module, so no pip install is required.

🔁 Run It Again

You can safely run:

python app.py


multiple times.

The script uses:

INSERT OR IGNORE


and the email column is unique, preventing duplicate sample users from being inserted.

🧹 Reset the Database

Want to start fresh?

Delete the database:

rm database.db


Then run:

python app.py


On Windows, you can simply delete database.db from File Explorer and run the application again.

📋 Requirements
Python 3.x
SQLite3 — included with Python
No third-party packages

Check your Python version:

python --version

🎯 Use Cases

This project is useful for:

🧪 Testing database-related code
📚 Learning SQLite
🐍 Practicing Python database operations
🔨 Prototyping small applications
💻 Creating a local development database
📜 License

This project is provided for learning, testing, and development purposes.

Feel free to modify and use it in your own projects.