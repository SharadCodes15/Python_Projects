# 💬 WhatTools

### Simple WhatsApp Message Automation with Python & PyAutoGUI

**WhatTools** is a lightweight WhatsApp message automation tool built with **Python** and **PyAutoGUI**.

It automates repetitive WhatsApp messaging tasks by controlling your computer's keyboard and mouse, interacting directly with the **WhatsApp Web or Desktop interface**.

> ⚠️ **Use responsibly.** Make sure your automation complies with WhatsApp's Terms of Service and applicable laws. Avoid unsolicited or spam messaging.

---

## ✨ Features

* 💬 **Automated Messaging** — Send WhatsApp messages automatically.
* 🖱️ **GUI Automation** — Uses PyAutoGUI for keyboard and mouse control.
* ⚡ **Lightweight** — Simple implementation with minimal dependencies.
* 🐍 **Python Powered** — Built entirely with Python.
* 📦 **Automatic Dependencies** — Dependencies are managed through `pyproject.toml`.
* 🖥️ **WhatsApp Web/Desktop** — Works with the WhatsApp interface running on your computer.
* 🔧 **Customizable** — Easy to modify and extend for your own automation workflows.
* 🧑‍💻 **Open Source** — Contributions and improvements are welcome.

---

## ⚠️ Important

WhatTools interacts with WhatsApp through **GUI automation**.

Before running the tool, make sure:

* ✅ WhatsApp Web or WhatsApp Desktop is already logged in.
* ✅ The WhatsApp window is open and visible.
* ✅ The WhatsApp interface is positioned correctly.
* ✅ Your screen resolution and display scaling do not interfere with mouse coordinates.
* ✅ You understand that UI changes may require updating automation coordinates.
* ✅ You use the tool responsibly and comply with WhatsApp's policies.

### Why does screen position matter?

PyAutoGUI interacts with elements based on their position on your screen. If the WhatsApp window moves or the interface changes, coordinates used by the automation may no longer work correctly.

---

## 📋 Requirements

Before installing WhatTools, make sure you have:

| Requirement     | Version / Details             |
| --------------- | ----------------------------- |
| 🐍 Python       | 3.10+                         |
| 🌐 WhatsApp     | WhatsApp Web or Desktop       |
| 📦 pip          | Latest recommended            |
| 🖥️ Environment | Graphical desktop environment |

### Check Python

```bash
python --version
```

On some Linux/macOS systems:

```bash
python3 --version
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/SharadCodes15/WhatTools.git
cd WhatTools
```

---

## 2. Create a Virtual Environment

Using a virtual environment is recommended to keep project dependencies isolated.

### 🪟 Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 🐧 Linux / 🍎 macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

Install the project and its dependencies using:

```bash
python -m pip install .
```

Dependencies defined in `pyproject.toml` will be installed automatically.

You don't need to install each dependency manually.

---

# ⚡ Usage

Once the installation is complete, start WhatTools with:

```bash
python main.py
```

Depending on your project configuration, you may also be able to run:

```bash
python app.py
```

Follow the instructions displayed by the application.

### Typical Workflow

```text
Start WhatTools
      │
      ▼
Open WhatsApp Web/Desktop
      │
      ▼
Make sure WhatsApp is logged in
      │
      ▼
Position the WhatsApp window correctly
      │
      ▼
Run the automation
      │
      ▼
Messages are sent automatically 🚀
```

---

# 📥 Install Directly from GitHub

You can also install WhatTools directly from the repository without manually cloning it:

```bash
python -m pip install git+https://github.com/SharadCodes15/WhatTools.git
```

### What happens?

```text
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
```

---

# 🧑‍💻 Development

If you want to modify the project, install it in **editable mode**:

```bash
python -m pip install -e .
```

Editable installation means changes to the source code can be tested without reinstalling the package after every modification.

### Development workflow

```bash
git clone https://github.com/SharadCodes15/WhatTools.git
cd WhatTools

python -m venv .venv
```

Activate the environment and then:

```bash
python -m pip install -e .
```

---

# 📁 Project Structure

```text
WhatTools/
│
├── 📄 app.py
├── 📄 main.py
├── 📄 pyproject.toml
├── 📄 README.md
├── 📄 .gitignore
└── 📁 .venv/          # Local virtual environment
```

> `.venv/` should normally be excluded from Git using `.gitignore`.

---

# 📦 Dependencies

Project dependencies are managed through:

```text
pyproject.toml
```

For example:

```toml
[project]
dependencies = [
    "pyautogui"
]
```

Install all project dependencies with:

```bash
python -m pip install .
```

This allows `pip` to automatically install everything defined by the project.

---

# 🔧 Customization

WhatTools is designed to be simple and easy to customize.

You can extend the project with features such as:

* ⏱️ Message scheduling
* 🔁 Repetitive task automation
* 📝 Custom message templates
* 📋 Multiple message workflows
* 🖱️ Custom screen coordinates
* ⌨️ Keyboard shortcuts
* ⚙️ User-configurable settings

Because the automation relies on PyAutoGUI, customizations may require adjustments depending on your screen resolution and WhatsApp UI layout.

---

# 🐛 Troubleshooting

### Automation clicks the wrong location

Check that:

* WhatsApp is in the expected position.
* Your display scaling has not changed.
* Your screen resolution matches the configuration.
* The WhatsApp UI has not changed.

### `python` command not found

Try:

```bash
python3 --version
```

If Python is not installed, install **Python 3.10 or newer** and make sure it is added to your system PATH.

### Dependencies are missing

Run:

```bash
python -m pip install .
```

Or, for development:

```bash
python -m pip install -e .
```

---

# 🤝 Contributing

Contributions, bug fixes, and improvements are welcome! ❤️

## Contribution Steps

### 1. Fork the repository

Create your own fork of the project.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/WhatTools.git
cd WhatTools
```

### 3. Create a feature branch

```bash
git checkout -b feature/my-feature
```

### 4. Make your changes

Implement and test your improvements.

### 5. Commit your changes

```bash
git add .
git commit -m "Add my feature"
```

### 6. Push your branch

```bash
git push origin feature/my-feature
```

### 7. Open a Pull Request

Create a Pull Request and describe the changes you made.

---

# 🐛 Reporting Issues

Found a bug?

Please open a GitHub Issue and include as much information as possible.

### Include:

* 🖥️ Operating system
* 🐍 Python version
* 📦 WhatTools version
* ❌ Error message
* 📝 Steps to reproduce the issue
* 📸 Screenshots, if applicable

Providing detailed information makes it much easier to diagnose and fix problems.

---

# ⭐ Support the Project

If you find **WhatTools** useful, consider giving the repository a ⭐.

It helps support the project and encourages further development! ❤️

---

# 📄 License

Add your project's license information here.

For example:

```text
MIT License
```

If you use an open-source license, consider adding a `LICENSE` file to the root of the repository.

---

## 💬 WhatTools

> Automate WhatsApp messaging with Python & PyAutoGUI.

**Made with ❤️ and 🐍 Python**

⭐ If you like the project, don't forget to star the repository!
