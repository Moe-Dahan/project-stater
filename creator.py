import os
import subprocess

parent_dir = "" # directory you like to store all work

user_folder_create = input("[+] Project Name!: ")

# creates the project and index.html file
project_dir = os.path.join(parent_dir, user_folder_create)
os.mkdir(project_dir)

index_file = os.path.join(project_dir, "index.html")
with open(index_file, "w") as index:
    index.write(f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{user_folder_create}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="assets/css/app.css">
    </head>
<body>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="assets/js/app.js"></script>
</body>
</html>
                    """)

# create the assets folder for css and js folders and files
assets_folder = os.path.join(project_dir, "assets")
os.mkdir(assets_folder)

# Create and write to the CSS and scss file
css_folder = os.path.join(assets_folder, "css")
os.mkdir(css_folder)

css_file_path = os.path.join(css_folder, "app.css")
scss_file_path = os.path.join(css_folder, "app.scss")

with open(css_file_path, "w") as file:
    file.write("/* css */\n")

with open(scss_file_path, "w") as file:
    file.write("/* scss */\n")

# Create the JavaScript directory inside assets
js_folder = os.path.join(assets_folder, "js")
os.mkdir(js_folder)

js_file_path = os.path.join(js_folder, "app.js")
with open(js_file_path, "w") as file:
    file.write("// js file\n")

# opens the project folder in vs code and runs vs code via powershell
subprocess.run(["code", project_dir], shell=True)
