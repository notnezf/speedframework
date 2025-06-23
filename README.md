# ⚡ Speedframework

Modular pentesting framework written in Python. Designed to automate common tasks such as port scanning, public information gathering (OSINT), and brute-force attacks.

---

## 🚀 Available Modules

- 🔍 **Scanner** – Fast TCP/UDP port scanning.
- 🕵️ **OSINT** – Public information gathering.
- 🛠️ **Brute** – Brute-force attacks against services like FTP, SSH, and Telnet.

---

## 📸 Screenshots

### Port Scanning
![Scan](assets/screenshots/scan.png)

### FTP Brute Force
![FTP Bruteforce](assets/screenshots/brute_ftp.png)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/speedframework.git
cd speedframework
pip install -r requirements.txt
```

---

## 🧑‍💻 Basic Usage

```bash
python3 -m speedframework --module brute --type ssh --ip 192.168.1.10 --userlist config/users.txt --passlist config/pass.txt
```

### Common Parameters

| Parameter         | Description                                     |
|------------------|-------------------------------------------------|
| `--module` / `-m` | Module to run (`brute`, `scanner`, `osint`)     |
| `--type` / `-t`   | Subtype within the module (e.g., `ftp`, `ssh`)  |
| `--ip` / `-i`     | Target IP or domain                             |
| `--userlist` / `-u` | Path to the username dictionary               |
| `--passlist` / `-p` | Path to the password dictionary               |

---

## 📁 Project Structure

```
speedframework/
├── speedframework/
│   ├── core/
│   │   ├── brute.py
│   │   ├── osint.py
│   │   └── scanner.py
│   ├── utils/
│   │   ├── common.py
│   │   ├── logger.py
│   │   └── print.py
│   ├── config/
│   │   ├── users.txt
│   │   └── pass.txt
│   └── __main__.py
├── assets/
│   └── screenshots/
│       ├── scan.png
│       └── brute_ftp.png
├── tests/
│   └── test_brute.py
├── requirements.txt
├── setup.py
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🧾 License

MIT License – free to use and modify.

---

## 👤 Author

Created by Ferrán Ortega.  
Educational project for learning and experimentation in cybersecurity.
