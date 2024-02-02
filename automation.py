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

def count_file_types(folder_path, file_extension):
    count = sum(1 for file in os.listdir(folder_path) if file.endswith(file_extension))
    console.print(f"[cyan]Number of '[magenta]{file_extension}[/magenta]' files in '[blue]{folder_path}[/blue]': [magenta]{count}[/magenta][/cyan]")

def main():
    while True:
        console.print("[bright_yellow]\n╔══════════════════════════════════════════╗[/bright_yellow]")
        console.print("[bright_yellow]║       [magenta]1. Create Folder                   [/magenta]║[/bright_yellow]")
        console.print("[bright_yellow]║       [magenta]2. Handle Deleted User             [/magenta]║[/bright_yellow]")
        console.print("[bright_yellow]║       [magenta]3. Sort Documents                  [/magenta]║[/bright_yellow]")
        console.print("[bright_yellow]║       [magenta]4. Parse Errors and Warnings       [/magenta]║[/bright_yellow]")
        console.print("[bright_yellow]║       [magenta]5. Count File Types                [/magenta]║[/bright_yellow]")
        console.print("[bright_yellow]║       [magenta]6. Exit                            [/magenta]║[/bright_yellow]")
        console.print("[bright_yellow]╚══════════════════════════════════════════╝[/bright_yellow]")

        choice = Prompt.ask("[blue]Choose a task (Enter the number)[/blue]", choices=['1', '2', '3', '4', '5', '6'], default='6')

        if choice == '1':
            folder_name = Prompt.ask("[blue]Enter folder name:[/blue]")
            create_folder(folder_name)
        elif choice == '2':
            user_folder = Prompt.ask("[blue]Enter user folder to handle deleted user:[/blue]")
            handle_deleted_user(user_folder)
        elif choice == '3':
            folder_path = Prompt.ask("[blue]Enter folder path to sort documents:[/blue]")
            sort_documents(folder_path)
        elif choice == '4':
            log_file = Prompt.ask("[blue]Enter log file path to parse errors:[/blue]")
            target_directory = Prompt.ask("[bold blue]Enter target directory for logs:[/blue]")
            parse_errors(log_file, target_directory)
        elif choice == '5':
            folder_path = Prompt.ask("[blue]Enter folder path to count file types:[/blue]")
            file_extension = Prompt.ask("[blue]Enter file extension:[/blue]")
            count_file_types(folder_path, file_extension)
        elif choice == '6':
            break
        else:
            console.print("[red]Invalid choice. Please enter a valid task number.[/red]")

if __name__ == "__main__":
    main()
