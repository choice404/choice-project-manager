"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

import click
from jinja2 import Environment, FileSystemLoader
import os
import shutil
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

@click.command()
@click.argument('cmdtype', type=click.Choice(['create', 'newfile']), default="create")
@click.argument('projectlanguage', type=click.Choice(list(LANGUAGES.keys())), default="py")
@click.argument('licensename', type=click.Choice(list(LICENSE.keys())), default="arr")
@click.option('-f', '--filename', help="The name of the newfile")
@click.option('-n', '--name', help="The name of the project")
@click.option('-d', '--desc', help="The description of the project")
@click.option('-a', '--auth', help="The name of the author of the project")
def main(cmdtype, projectlanguage, licensename, filename, name, desc, auth):
    print(os.path.dirname(os.path.abspath(__file__)))

    if cmdtype == "newfile":
        if not filename:
            filename = click.prompt("Enter filename")

        projectLanguage = None

        curPath = os.getcwd()
        traversePath = curPath
        while traversePath != os.path.dirname(traversePath):
            projectEnv = os.path.join(curPath, ".project.env")
            if(os.path.exists(projectEnv)) and os.path.isfile(projectEnv):
                load_dotenv(dotenv_path=projectEnv)
                projectName = os.getenv("projectName")
                projectDescription = os.getenv("projectDescription")
                projectAuthor = os.getenv("projectAuthor")
                licenseName = os.getenv("licenseName")
                projectLanguage = os.getenv("projectLanguage")
                year = os.getenv("year")
                break

        projectLanguage = LANGUAGES_REVERSE[str(projectLanguage)]
        templateVars = os.environ
        while projectLanguage not in LANGUAGES.keys():
            projectLanguage = click.prompt("Enter project language")

        if projectLanguage == "html":
            tailwind = click.prompt("Do you want to use tailwindcss? (y/n)")
            templateVars["tailwind"] = tailwind

        filename = f'{filename}.{projectLanguage}'
        templateFile = os.path.join(os.path.dirname(os.path.abspath(__file__)),f'templates/newfile/template.{projectLanguage}')
        templateDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),f'templates/newfile')
        env = Environment(loader=FileSystemLoader(templateDir, followlinks=True), autoescape=False)

        if projectLanguage == "c++" and filename == "main.cpp":
            templateFile = os.path.join(os.path.dirname(os.path.abspath(__file__)),f'templates/newfile/templateMain.cpp')

        template = env.get_template(os.path.basename(templateFile))
        renderedContent = template.render(**templateVars)
        outputPath = os.path.join(curPath, filename)

        with open(outputPath, 'w') as output_file:
            output_file.write(renderedContent)

        print(f'File "{filename}" created successfully.')

    elif cmdtype == "create":
        if not name:
            name = click.prompt("Enter project name")
        if not desc:
            desc = click.prompt("Enter project description")
        if not auth:
            auth = click.prompt("Enter project author name")

        projectLang = LANGUAGES[projectlanguage]
        projectLicense = LICENSE[licensename]

        templateDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),f'templates/{LANGUAGES[projectlanguage]}')
        os.makedirs(name)
        envPath = os.path.join(name, '.project.env')

        with open(envPath, 'w') as file:
            file.write(f'''projectName="{ name }"
projectDescription="{ desc }"
projectAuthor="{ auth }"
licenseName="{ projectLicense }"
projectLanguage="{ projectLang }"
year="{ date.today().year }"''')

        os.chdir(name)

        dotenvPath = os.path.join(os.getcwd(), '.project.env')
        load_dotenv(dotenvPath)

        os.chdir('../')

        env = Environment(loader=FileSystemLoader(templateDir, followlinks=True), autoescape=False)

        templateVars = os.environ

        for root, dirs, files in os.walk(templateDir):
            for file in files:
                templatePath = os.path.join(root, file)
                relativePath = os.path.relpath(templatePath, templateDir)
                outputPath = os.path.join(name, relativePath)

                os.makedirs(os.path.dirname(outputPath), exist_ok=True)

                template = env.get_template(relativePath)
                renderedContent = template.render(**templateVars)
                with open(outputPath, 'w') as output_file:
                    output_file.write(renderedContent)

        print(f'Project "{name}" created successfully.')

if __name__ == "__main__":
    main()

"""
Copyright (C) 2023 Austin Choi

choiProjectManager

A template managing project to create new projects

This code is licensed under the GNU General Public License 3.0.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
