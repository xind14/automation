from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
import re
import shutil

console = Console()

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        console.print(f"[red]Folder '[blue]{folder_name}[/blue]' created successfully.[/red]")
    except FileExistsError:
        console.print(f"[red]Folder '[blue]{folder_name}[/blue]' already exists.[/red]")

def handle_deleted_user(user_folder):
    user_folder_path = f"assets/user_docs/{user_folder}"
    temp_folder = "temporary_folder"

    try:
        if os.path.exists(user_folder_path):
            if not os.path.exists(temp_folder):
                os.mkdir(temp_folder)

            shutil.move(user_folder_path, temp_folder)
            console.print(f"Successfully moved user '[green]{user_folder}[/green]' documents to [blue]{temp_folder}[/blue].")
    except FileNotFoundError:
        console.print(f"User '[green]{user_folder}[/green]' folder not found.")

def sort_documents(folder_path):

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file_name)

            destination_folder = os.path.join(folder_path, file_extension[1:])
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            destination_path = os.path.join(destination_folder, file_name)
            shutil.move(file_path, destination_path)

    console.print(f"[yellow]Documents sorted into new folders in {folder_path}.[/yellow]")

def parse_errors(log_file, target_directory):
    with open(log_file, 'r') as file:
        log_content = file.read()

    errors = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, ERROR: (.+)', log_content)
    warnings = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, WARNING: (.+)', log_content)

    with open(os.path.join(target_directory, 'errors.log'), 'w') as errors_file:
        for error in errors:
            errors_file.write(f"{error}\n")
        console.print(f"[green]Errors logged to [blue]{os.path.join(target_directory, 'errors.log')}[/blue][/green]")

    with open(os.path.join(target_directory, 'warnings.log'), 'w') as warnings_file:
        for warning in warnings:
            warnings_file.write(f"{warning}\n")
        console.print(f"[yellow]Warnings logged to [blue]{os.path.join(target_directory, 'warnings.log')}[/blue][/yellow]")

