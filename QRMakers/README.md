# SAM QR

> A lightweight and extensible QR Code Generator built with Python.

**SAM QR** is a Python-based QR code generator designed with a simple architecture and multiple interfaces in mind.

The **CLI version is currently available**, while **TUI and Web GUI versions are coming soon**.

---

## ✨ Features

### Current — CLI

* Generate QR codes from URLs or text
* Save QR codes as PNG images
* Interactive command-line interface
* Clean terminal UI with borders and colors
* Input validation
* Simple and reusable Python class
* Easy to extend

### 🚧 Coming Soon

* 🖥️ **TUI Version** — Terminal User Interface
* 🌐 **Web GUI Version** — Browser-based interface
* 🎨 More QR customization options
* 📁 Custom output directories
* ⚙️ Advanced QR configuration
* 📦 Additional export formats

---

## 📸 Interface

### CLI

```text
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                       SAM QR                                 ║
║                  QR CODE GENERATOR                           ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║        ▣  Generate QR Codes                                  ║
║        ▣  Save QR Codes                                      ║
║        ▣  Fast • Simple • Secure                             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 🛠️ Requirements

* Python **3.9+**
* `qrcode`
* `Pillow`

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/sam-qr.git
cd sam-qr
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Start the CLI:

```bash
python cli.py
```

You should see the SAM QR interface:

```text
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                       SAM QR                                 ║
║                  QR CODE GENERATOR                           ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   [1]  Generate QR Code                                      ║
║   [2]  Generate & Save QR Code                               ║
║   [3]  About                                                 ║
║   [4]  Exit                                                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

Choose an option and follow the prompts.

---

## 🐍 Python API

SAM QR can also be used programmatically.

Example:

```python
from main import QRCodeGenerator

qr = QRCodeGenerator()

qr.generateQR("https://example.com")

qr.saveQR("qr.png")
```

This generates a QR code and saves it as:

```text
qr.png
```

---

## 📁 Project Structure

```text
sam-qr/
│
├── main.py              # QR Code generation logic
├── cli.py               # CLI interface
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
│
├── output/              # Generated QR codes
│
└── ...
```

As the project grows, the interface layers may be organized like:

```text
sam-qr/
│
├── core/
│   └── qr_generator.py
│
├── cli/
│   └── cli.py
│
├── tui/
│   └── tui.py            # Coming soon
│
├── web/
│   └── app.py            # Coming soon
│
├── output/
│
├── requirements.txt
└── README.md
```

---

## 🧩 Planned Interfaces

SAM QR is being developed with multiple interfaces.

### 1. CLI — ✅ Available

The current version provides an interactive command-line interface.

```text
Terminal
   │
   ▼
┌───────────────┐
│    SAM QR     │
│     CLI       │
└───────┬───────┘
        │
        ▼
   QR Generator
```

### 2. TUI — 🚧 Coming Soon

A full Terminal User Interface with a richer interactive experience.

Planned features may include:

* Keyboard navigation
* Interactive forms
* QR configuration panels
* File browser
* Preview screen
* Better terminal layouts

```text
┌──────────────────────────────────────────────┐
│                  SAM QR                      │
├──────────────────────────────────────────────┤
│                                              │
│  URL: https://example.com                    │
│                                              │
│  [ Generate ]       [ Save ]                 │
│                                              │
│                  QR PREVIEW                  │
│                                              │
└──────────────────────────────────────────────┘
```

### 3. Web GUI — 🚧 Coming Soon

A browser-based interface for generating QR codes.

Planned features:

* Modern web interface
* URL/text input
* QR preview
* Download button
* QR customization
* Responsive design

```text
Browser
   │
   ▼
┌──────────────────────┐
│       SAM QR         │
│                      │
│  Enter URL / Text    │
│  ┌────────────────┐  │
│  │                │  │
│  └────────────────┘  │
│                      │
│     [ Generate ]     │
│                      │
│       ▣ ▣ ▣          │
│       ▣   ▣          │
│       ▣ ▣ ▣          │
│                      │
│      [ Download ]    │
└──────────────────────┘
```

---

## ⚙️ Configuration

The QR generator currently uses:

```python
qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
```

### Parameters

| Parameter  | Description               |
| ---------- | ------------------------- |
| `version`  | Controls the QR code size |
| `box_size` | Size of each QR pixel     |
| `border`   | Border thickness          |

The configuration will become more customizable in future releases.

---

## 🗺️ Roadmap

### Phase 1 — CLI

* [x] QR generation
* [x] URL/text input
* [x] PNG export
* [x] Interactive menu
* [x] Terminal styling
* [x] Basic validation

### Phase 2 — TUI

* [ ] Full terminal interface
* [ ] Keyboard navigation
* [ ] QR preview
* [ ] Configuration panel
* [ ] File management
* [ ] Improved UX

### Phase 3 — Web GUI

* [ ] Web interface
* [ ] QR preview
* [ ] Download functionality
* [ ] Customization controls
* [ ] Responsive layout

### Phase 4 — Advanced Features

* [ ] Multiple export formats
* [ ] Custom colors
* [ ] Logo support
* [ ] Error correction settings
* [ ] Batch QR generation
* [ ] Custom output directories

---

## 🤝 Contributing

Contributions, ideas, and improvements are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/my-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add my feature"
```

5. Push the branch

```bash
git push origin feature/my-feature
```

6. Open a Pull Request

---

## 🐛 Issues

Found a bug or have a feature request?

Please open an issue and include:

* Python version
* Operating system
* Steps to reproduce the issue
* Error message, if any
* Expected behavior

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

## 👨‍💻 Author

**SAM QR**

Built with ❤️ and Python.

---

## ⭐ Support

If you find SAM QR useful, consider giving the repository a ⭐ on GitHub.

More interfaces are coming soon:

```text
                 SAM QR
                   │
       ┌───────────┼───────────┐
       │           │           │
       ▼           ▼           ▼
      CLI         TUI        WEB GUI
    ✅ NOW     🚧 SOON     🚧 SOON
```

**SAM QR — Generate. Scan. Share.**
