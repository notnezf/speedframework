# ⚡ Speedframework

Framework modular de pentesting escrito en Python. Diseñado para automatizar tareas comunes como escaneo de puertos, recolección de información pública (OSINT) y ataques de fuerza bruta.

---

## 🚀 Módulos disponibles

- 🔍 **Scanner** – Escaneo rápido de puertos TCP/UDP.
- 🕵️ **OSINT** – Recolección de información pública.
- 🛠️ **Brute** – Ataques de fuerza bruta contra servicios como FTP, SSH y Telnet.

---

## 📸 Capturas de pantalla

### Escaneo de puertos
![Escaneo](assets/screenshots/scan.png)

### Fuerza bruta FTP
![FTP Bruteforce](assets/screenshots/brute_ftp.png)

---

## 📦 Instalación

```bash
git clone https://github.com/tuusuario/speedframework.git
cd speedframework
pip install -r requirements.txt
```

---

## 🧑‍💻 Uso básico

```bash
python3 -m speedframework --module brute --type ssh --ip 192.168.1.10 --userlist config/users.txt --passlist config/pass.txt
```

### Parámetros comunes

| Parámetro       | Descripción                          |
|----------------|--------------------------------------|
| `--module` / `-m`   | Módulo a ejecutar (`brute`, `scanner`, `osint`) |
| `--type` / `-t`     | Subtipo dentro del módulo (ej. `ftp`, `ssh`)   |
| `--ip` / `-i`       | IP o dominio objetivo             |
| `--userlist` / `-u` | Ruta al diccionario de usuarios   |
| `--passlist` / `-p` | Ruta al diccionario de contraseñas |

---

## 📁 Estructura del proyecto

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

## 🧾 Licencia

MIT License – libre uso y modificación.

---

## 👤 Autor

Creado por [tu nombre o alias].  
Proyecto educativo con fines de aprendizaje y experimentación en ciberseguridad.
```
