"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

import click
from jinja2 import Environment, FileSystemLoader
import os
from dotenv import load_dotenv
from datetime import date

LANGUAGES = {
    "py": "python",
    "c": "c",
    "cpp": "c++",
    "h": "c++",
    "hpp": "c++",
    "cs": "c#",
    "sh": "bash",
    "ng": "angular",
    "java": "java",
    "js": "javascript",
    "ts": "typescript",
    "html": "html",
    "css": "css",
    "scss": "scss",
    "rs": "rust",
    "lua": "lua",
    "sql": "sql",
    "r": "r",
    "asm": "assembly",
    "cmine": "cmine",
    "lpu": "lpu",
    "" : "",
}

ALL_LANGUAGES = {
    "py": "python",
    "c": "c",
    "cpp": "c++",
    "h": "c++",
    "hpp": "c++",
    "cs": "c#",
    "sh": "bash",
    "ng": "angular",
    "java": "java",
    "js": "javascript",
    "ts": "typescript",
    "html": "html",
    "css": "css",
    "scss": "scss",
    "sass": "sass",
    "go": "go",
    "rs": "rust",
    "php": "php",
    "rb": "ruby",
    "kt": "kotlin",
    "swift": "swift",
    "scala": "scala",
    "hs": "haskell",
    "lua": "lua",
    "dart": "dart",
    "sql": "sql",
    "pl": "perl",
    "r": "r",
    "mat": "matlab",
    "asm": "assembly",
    "cmine": "cmine",
    "lpu": "lpu",
}

LANGUAGES_REVERSE = {
    "python": "py",
    "c": "c",
    "c++": "cpp",
    "h": "h",
    "hpp": "hpp",
    "c#": "cs",
    "bash": "sh",
    "angular": "ng",
    "java": "java",
    "javascript": "js",
    "typescript": "ts",
    "html": "html",
    "css": "css",
    "scss": "scss",
    "sass": "sass",
    "go": "go",
    "rs": "rust",
    "php": "php",
    "ruby": "rb",
    "kotlin": "kt",
    "swift": "swift",
    "scala": "scala",
    "haskell": "hs",
    "lua": "lua",
    "dart": "dart",
    "sql": "sql",
    "pl": "perl",
    "r": "r",
    "mat": "matlab",
    "assembly": "asm",
    "cmine": "cmine",
    "lpu": "lpu",
}

LICENSE = {
    "gnu": "GNU General Public License 3.0",
    "mit": "MIT License",
    "arr": "All rights reserved"
}

script_dir = os.path.dirname(os.path.abspath(__file__))
script_env = os.path.join(script_dir, ".chpm.env")

if not os.path.exists(script_env):
    with open(script_env, 'w') as file:
        file.write(f'''TEMPLATE_DIR=""''')

load_dotenv(dotenv_path=script_env)

template_dir = os.getenv("TEMPLATE_DIR")

@click.command()
@click.argument('cmd', type=click.Choice(['create', 'newfile', 'set', '']), default="")
@click.argument('language', type=click.Choice(list(LANGUAGES.keys())), default="")
@click.argument('license_name', type=click.Choice(list(LICENSE.keys())), default="arr")
@click.option('-f', '--filename', help="The name of the newfile")
@click.option('-n', '--name', help="The name of the project")
@click.option('-d', '--desc', help="The description of the project")
@click.option('-a', '--auth', help="The name of the author of the project")
@click.option('-ls', '--list', 'list_templates', is_flag=True, help="List all available templates")
@click.option('-s', '--set', 'set_template', is_flag=True, help="Set the current directory as the template directory")
@click.option('-l', '--license', 'list_license', is_flag=True, help="List all available licenses")
def main(cmd, language, license_name, filename, name, desc, auth, list_templates, set_template, list_license):
    '''
    A template managing project to create new projects and files using templates
            
            Parameters:
                    cmd (str): The command to execute
                    language (str): The language of the project
                    license_name (str): The license of the project
                    filename (str): The name of the file
                    name (str): The name of the project
                    desc (str): The description of the project
                    auth (str): The name of the author of the project
                    list_templates (bool): List all available templates
                    set_template (bool): Set the current directory as the template directory
                    list_license (bool): List all available licenses
            Returns:
                    None
    '''
    if template_dir == "" and cmd != "set" and not set_template:
        print('''Please set the template directory
Syntax: chpm2 set''')
        return

    if language == "" and cmd == "create":
        print('''Please specify the language
Syntax: chpm create <language> <license?>''')
        return

    if cmd == "set" or set_template:
        set_template_dir()
    if list_templates:
        print("Available templates:")
        for template in ALL_LANGUAGES.keys():
            print(template)
    elif list_license:
        print("Available licenses:")
        for license in LICENSE.keys():
            print(license)
    elif cmd == "newfile":
        newfile(filename, language)
    elif cmd == "create":
        create(name, desc, auth, language, license_name)

def set_template_dir():
    '''
    Sets the current directory as the template directory
        
            Parameters:
                    None
            Returns:
                    None
    '''
    current_path = os.getcwd()
    template_dir_prompt = click.prompt(f'Set {current_path} as the template directory? (y/n)')
    if template_dir_prompt.lower() == "y":
        with open(script_env, 'w') as file:
            file.write(f'''TEMPLATE_DIR="{current_path}"''')
        print(f'{current_path} set as the template directory.')
    elif(template_dir_prompt.lower() == 'n'):
        return
    else:
        print("Invalid choice")

def create(name, desc, auth, language, license_name):
    '''
    Creates a new project using the project information or a specified language

            Parameters:
                    name (str): The name of the project
                    desc (str): The description of the project
                    auth (str): The name of the author of the project
                    language (str): The language of the project
                    license_name (str): The license of the project
            Returns:
                    None
    '''
    if not name:
        name = click.prompt("Enter project name")
    if not desc:
        desc = click.prompt("Enter project description")
    if not auth:
        auth = click.prompt("Enter project author name")

    project_lang = LANGUAGES[language]
    project_license = LICENSE[license_name]

    target_template_dir = f'{template_dir}/{LANGUAGES[language]}'
    os.makedirs(name)
    env_path = os.path.join(name, '.project.env')

    with open(env_path, 'w') as file:
        file.write(f'''projectName="{ name }"
projectDescription="{ desc }"
projectAuthor="{ auth }"
licenseName="{ project_license }"
projectLanguage="{ project_lang }"
year="{ date.today().year }"''')

    os.chdir(name)

    dotenv_path = os.path.join(os.getcwd(), '.project.env')
    load_dotenv(dotenv_path)

    os.chdir('../')

    env = Environment(loader=FileSystemLoader(target_template_dir, followlinks=True), autoescape=False)

    template_vars = os.environ

    for root, dirs, files in os.walk(target_template_dir):
        for file in files:
            template_path = os.path.join(root, file)
            relative_path = os.path.relpath(template_path, target_template_dir)
            output_path = os.path.join(name, relative_path)

            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            template = env.get_template(relative_path)
            rendered_content = template.render(**template_vars)
            with open(output_path, 'w') as output_file:
                output_file.write(rendered_content)

    print(f'Project "{name}" created successfully.')

def newfile(filename, language):
    '''
    Creates a new file using the project information or a specified language

            Parameters:
                    filename (str): The name of the file
                    language (str): The language of the file
            Returns:
                    None
    '''
    if not filename:
        filename = click.prompt("Enter filename")

    project_language = ""

    if language != "":
        project_language = language

    current_path = os.getcwd()
    traverse_path = current_path
    while traverse_path != os.path.dirname(traverse_path):
        project_env = os.path.join(traverse_path, ".project.env")
        traverse_path = os.path.dirname(traverse_path)
        if(os.path.exists(project_env)) and os.path.isfile(project_env):
            load_dotenv(dotenv_path=project_env)
            if language == "":
                project_language = LANGUAGES_REVERSE[str(os.getenv("projectLanguage"))]
            break

    template_vars = os.environ
    # while project_language not in LANGUAGES.keys():
    #     project_language = click.prompt("Enter project language")

    if project_language == "html":
        tailwind = click.prompt("Do you want to use tailwindcss? (y/n)")
        template_vars["tailwind"] = tailwind

    filename = f'{filename}.{project_language}'
    template_file = f'{template_dir}/newfile/template.{project_language}'
    target_template_dir = f'{template_dir}/newfile'
    env = Environment(loader=FileSystemLoader(target_template_dir, followlinks=True), autoescape=False)

    if filename == "main.cpp":
        template_file = f'{template_dir}/newfile/templateMain.cpp'

    template = env.get_template(os.path.basename(template_file))
    rendered_content = template.render(**template_vars)
    output_path = os.path.join(current_path, filename)

    with open(output_path, 'w') as output_file:
        output_file.write(rendered_content)

    print(f'File "{filename}" created successfully.')

def log(message):
    print(message)

if __name__ == "__main__":
    main()

"""
Copyright (C) 2023 Austin Choi

choiProjectManager

A template managing project to create new projects

This code is licensed under the GNU General Public License 3.0.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
