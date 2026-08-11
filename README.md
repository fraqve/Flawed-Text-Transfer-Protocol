# FTTP — Flawed Text Transfer Protocol

A custom HTTP-inspired network protocol built from scratch in Python. No frameworks, no dependencies, just raw sockets and bad decisions.

I built this to understand how protocols actually work under the hood — how two machines agree on a format, how requests and responses are structured, and why HTTP makes the design choices it does. The best way to understand something is to build a worse version of it yourself.

---

## What it does

FTTP is a client-server protocol that runs over TCP. It supports:

- `GET` — request a file from the server
- `UPLOAD` — send a file to the server
- `SEND` — server-side response method, delivers the requested file or error back to the client

---

## Project structure

```
fttp/
├── fttp.py        # Protocol library (shared by server and client)
├── server.py      # FTTP server
├── init.py        # Generates error pages (run this first — yes it hardcodes every single HTML page individually, no I'm not sorry)
└── config.json    # Server configuration
```

---

## Setup

**1. Create your config.json**

```json
{
    "ROOT_DIRECTORY": "/var/www/html"
}
```

Point `ROOT_DIRECTORY` at wherever you want the server to serve files from.

**2. Run init.py**

```bash
python3 init.py
```

This generates the error pages (400, 404, 401, 501, 502, 505) in your root directory. If you skip this step the server still works — error responses will just return a blank page. You were warned.

**3. Drop some files in your root directory**

```bash
echo "<html><p>hello from fttp</p></html>" > /var/www/html/index.html
```

**4. Start the server**

```bash
python3 server.py
```

Server listens on port `1404` by default.

---

## Usage

### GET a file
using netcat

```bash
nc 127.0.0.1 1404
FTTP GET index.html
```

### UPLOAD a file


```bash
nc 127.0.0.1 1404
FTTP UPLOAD hello.txt
hello world
[blank line to terminate]
```

---

## Request format

```
FTTP <METHOD> <filepath>\r\n
```

## Response format

```
FTTP SEND <filepath> <code> <message>\r\n
<body>\r\n\r\n
```

---

## Status codes

| Code | Meaning |
|------|---------|
| 200  | OK — request succeeded |
| 400  | Trash Request — your request is malformed |
| 404  | File Not Found |
| 401  | Path is a Directory |
| 501  | Permission Error |
| 502  | OS Error |
| 505  | Unknown Exception |

---

## Known limitations

- **Binary uploads are unreliable** — FTTP uses `\r\n\r\n` as the upload terminator. Binary files (images, video, audio) can contain this byte sequence naturally, which will corrupt the transfer. Text files work fine.
- **No encryption** — everything is plaintext over TCP. Don't use this for anything sensitive.
- **No concurrent connections** — the server handles one connection at a time. Multiple simultaneous clients will queue up.
- **No persistent keep-alive** — each connection handles one request then closes.

---

## Why

I wanted to understand what happens between a browser typing a URL and a server sending back HTML. The answer turns out to be: two programs exchanging text over a socket, following rules they both agreed on in advance.

FTTP is my protocol where i designed the rules myself. It's messier than HTTP and missing about 90% of its features.

---

## Requirements

- Python 3.13+
- No external dependencies
