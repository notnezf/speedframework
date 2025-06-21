```markdown
# 🛠️ Pentesting Toolkit (CLI Framework)

Modular and extensible CLI-based toolkit for penetration testing, information gathering, scanning, and brute-force attacks — built in Python for learning and rapid experimentation.

## 🚀 Features

- 🧠 **Modular design**: Brute-force, OSINT, scanning, and logging modes.
- 🔐 **Brute-force support**: FTP and SSH (HTTP in progress).
- 🌐 **Custom port targeting**: Supports non-default ports (e.g. SSH on 2220).
- 🗂️ **File-based input**: Accepts custom user/password wordlists.
- 📜 **Verbose output**: Optional logs and detailed result tracking.

## 🧩 Usage

```bash
python main.py -m <mode> -t <type> -i <target> [options]
```

### Available Modes

| Mode     | Description                            | Required Options             |
|----------|----------------------------------------|-------------------------------|
| `brute`  | Brute-force attack                     | `-t`, `-i`, `-u`, `-p`        |
| `osint`  | Information gathering                  | `-t`, `-i`                    |
| `scanner`| Port/service scanning                  | `-t`, `-i`                    |
| `logger` | Log-related utilities (WIP)            | `-t`, `-i`                    |

### Example: Brute-force SSH

```bash
python main.py -m brute -t ssh -i bandit.labs.overthewire.org \
-u users.txt -p passwords.txt --port 2220 --verbose
```

## 📁 File Format

- **Userlist**: One username per line.
- **Passlist**: One password per line.

## 📦 Requirements

- Python 3.7+
- Dependencies:
  - `paramiko` (for SSH)
  - `click`
  - `ftplib` (standard)

Install them with:

```bash
pip install -r requirements.txt
```

## ✅ Status

| Module    | Status       |
|-----------|--------------|
| Brute FTP | ✅ Completed |
| Brute SSH | ✅ Completed |
| HTTP Form | ⚙️ In Progress |
| OSINT     | ⚙️ In Progress |
| Scanner   | 🔜 Planned    |
| Logger    | 🔜 Planned    |

## 📄 License

This project is for **educational and ethical hacking purposes** only. Use responsibly.

---

## 🧠 Author

Made by Ferrán — for learning, experimenting, and breaking things the right way.
