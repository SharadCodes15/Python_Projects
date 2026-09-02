💬 WhatTools

🐍 A simple WhatsApp message automation tool built with Python and PyAutoGUI.

WhatTools allows you to automate sending WhatsApp messages using your computer's keyboard and mouse through PyAutoGUI
.

It is designed to automate repetitive WhatsApp messaging tasks while keeping the implementation simple and lightweight.

✨ Features
💬 Send WhatsApp messages automatically
🖱️ Mouse and keyboard automation using PyAutoGUI
⚡ Simple and lightweight
🐍 Built entirely with Python
📦 Dependencies are installed automatically
🖥️ Works with the WhatsApp Web/Desktop interface
🔧 Easy to customize and extend
⚠️ Important

WhatTools controls WhatsApp through GUI automation.

Make sure:

WhatsApp Web/Desktop is already logged in.
The WhatsApp window is visible and positioned correctly.
Your screen resolution/scaling does not interfere with mouse coordinates.
You use the tool responsibly and comply with WhatsApp's terms and policies.

Because PyAutoGUI interacts with the screen, changes to the WhatsApp UI or window position may require adjustments.

📋 Requirements
🐍 Python 3.10+
🌐 WhatsApp Web or WhatsApp Desktop
📦 pip
🖥️ A graphical desktop environment

Check your Python version:

python --version

🚀 Installation
1. Clone the Repository
git clone https://github.com/SharadCodes15/WhatTools.git
cd WhatTools


2. Create a Virtual Environment

Using a virtual environment is recommended.

🪟 Windows
python -m venv .venv
.venv\Scripts\activate

🐧 Linux / 🍎 macOS
python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

Install WhatTools using:

python -m pip install .


All dependencies defined in pyproject.toml will be downloaded and installed automatically.

⚡ Usage

Start the application with:

python main.py


Depending on your implementation, you may also be able to run:

python app.py


Once the application starts, follow the instructions displayed by the tool.

📥 Install Directly from GitHub

You can install WhatTools directly from GitHub without manually cloning the repository:

python -m pip install git+https://github.com/SharadCodes15/WhatTools.git


pip will automatically:

GitHub Repository
       │
       ▼
   Download Code
       │
       ▼
 Read pyproject.toml
       │
       ▼
Install Dependencies
       │
       ▼
   WhatTools Ready 🚀

🧑‍💻 Development

For development, install the project in editable mode:

python -m pip install -e .


This means changes to your source code can be tested without reinstalling the package every time.

📁 Project Structure
WhatTools/
│
├── 📄 app.py
├── 📄 main.py
├── 📄 pyproject.toml
├── 📄 README.md
├── 📄 .gitignore


📦 Dependencies

Project dependencies are managed through:

pyproject.toml


For example:

[project]
dependencies = [
    "pyautogui"
]


You don't need to manually install each dependency.

Simply run:

python -m pip install .


and pip will install everything specified in pyproject.toml.

🤝 Contributing

Contributions and improvements are welcome! ❤️

Fork the repository
Create a branch
git checkout -b feature/my-feature

Make your changes
Commit them
git add .
git commit -m "Add my feature"

Push your branch
git push origin feature/my-feature

Open a Pull Request 🚀
🐛 Reporting Issues

If you encounter a problem, please open a GitHub issue and include:

🖥️ Operating system
🐍 Python version
📦 WhatTools version
❌ Error message
📝 Steps to reproduce the issue
⭐ Support

If you find WhatTools useful, consider giving the repository a ⭐.

It helps support the project and encourages further development.


💬 WhatTools

Automate WhatsApp messaging with Python & PyAutoGUI.

Made with ❤️ and 🐍 Python
