import os
import json

try:
    with open("config.json") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Config file not found")
    exit(1)

try:
    os.makedirs(config["ROOT_DIRECTORY"],exist_ok=True)
except PermissionError:
    print("permission denied")
    exit(1)
except KeyError:
    print("key ROOT_DIRECTORY not found")
    exit(1)
except Exception as e:
    print(e)
    exit(1)

with open(f"{config["ROOT_DIRECTORY"]}/400.html","w") as file:
    file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>400 - Trash Request</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: system-ui, -apple-system, sans-serif;
            background-color: #f8f9fa;
            color: #212529;
        }
        h1 {
            font-size: 7rem;
            margin: 0;
            font-weight: 800;
            color: #dc3545;
        }
        p {
            font-size: 1.5rem;
            margin-top: 0.5rem;
            color: #6c757d;
            text-transform: capitalize;
        }
    </style>
</head>
<body>
    <h1>400</h1>
    <p>Trash Request</p>
</body>
</html>""")

with open(f"{config["ROOT_DIRECTORY"]}/404.html","w") as file:
    file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>404 - File not found</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: system-ui, -apple-system, sans-serif;
            background-color: #f8f9fa;
            color: #212529;
        }
        h1 {
            font-size: 7rem;
            margin: 0;
            font-weight: 800;
            color: #dc3545;
        }
        p {
            font-size: 1.5rem;
            margin-top: 0.5rem;
            color: #6c757d;
            text-transform: capitalize;
        }
    </style>
</head>
<body>
    <h1>404</h1>
    <p>File not found server is as messy as a dumpster</p>
</body>
</html>""")

with open(f"{config["ROOT_DIRECTORY"]}/401.html","w") as file:
    file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>401 - Path is a directory</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: system-ui, -apple-system, sans-serif;
            background-color: #f8f9fa;
            color: #212529;
        }
        h1 {
            font-size: 7rem;
            margin: 0;
            font-weight: 800;
            color: #dc3545;
        }
        p {
            font-size: 1.5rem;
            margin-top: 0.5rem;
            color: #6c757d;
            text-transform: capitalize;
        }
    </style>
</head>
<body>
    <h1>401</h1>
    <p>Path is a directory</p>
</body>
</html>""")

with open(f"{config["ROOT_DIRECTORY"]}/501.html","w") as file:
    file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>501 - Permission error</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: system-ui, -apple-system, sans-serif;
            background-color: #f8f9fa;
            color: #212529;
        }
        h1 {
            font-size: 7rem;
            margin: 0;
            font-weight: 800;
            color: #dc3545;
        }
        p {
            font-size: 1.5rem;
            margin-top: 0.5rem;
            color: #6c757d;
            text-transform: capitalize;
        }
    </style>
</head>
<body>
    <h1>501</h1>
    <p>Permission error</p>
</body>
</html>""")

with open(f"{config["ROOT_DIRECTORY"]}/502.html","w") as file:
    file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>502 - OS error</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: system-ui, -apple-system, sans-serif;
            background-color: #f8f9fa;
            color: #212529;
        }
        h1 {
            font-size: 7rem;
            margin: 0;
            font-weight: 800;
            color: #dc3545;
        }
        p {
            font-size: 1.5rem;
            margin-top: 0.5rem;
            color: #6c757d;
            text-transform: capitalize;
        }
    </style>
</head>
<body>
    <h1>502</h1>
    <p>OS error</p>
</body>
</html>""")

with open(f"{config["ROOT_DIRECTORY"]}/505.html","w") as file:
    file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>505 unknown exception</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: system-ui, -apple-system, sans-serif;
            background-color: #f8f9fa;
            color: #212529;
        }
        h1 {
            font-size: 7rem;
            margin: 0;
            font-weight: 800;
            color: #dc3545;
        }
        p {
            font-size: 1.5rem;
            margin-top: 0.5rem;
            color: #6c757d;
            text-transform: capitalize;
        }
    </style>
</head>
<body>
    <h1>505</h1>
    <p>unknown exception</p>
</body>
</html>""")