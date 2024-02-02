from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
import re
import shutil




def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        console.print(f"[red]folder '[bold blue]{folder_name}[/bold blue]' created successfully.[/red]")
    except FileExistsError:
        console.print(f"[red]Folder '[bold blue]{folder_name}[/bold blue]' already exists.[/red]")


def handle_deleted_user(user_folder):
    user_folder_path = f"assets/user_docs/{user_folder}"
    temp_folder = "temporary_folder"

    try:
        if os.path.exists(user_folder_path):
            if not os.path.exists(temp_folder):
                os.mkdir(temp_folder)

            shutil.move(user_folder_path, temp_folder)
            print(f"Successfully moved user '[bold green]{user_folder}[/bold green]' documents to [bold blue]{temp_folder}[/bold blue].")
    except FileNotFoundError:
        print(f"User '[bold green]{user_folder}[/bold green]' folder not found.")

def sort_documents(folder_path):
    console = Console()

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file_name)
            file_extension = file_extension[1:].lower()

            destination_folder = os.path.join(folder_path, file_extension)
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            destination_path = os.path.join(destination_folder, file_name)
            shutil.move(file_path, destination_path)

    console.print(f"[yellow]Documents sorted into new folders in {folder_path}.[/yellow]")


# 4. **Parse a log file for errors and warnings:**
#    - From the previous task, you’ve moved a log file into the logs folder. Now, parse the log file for errors and warnings and create two separate log files in a target directory:
#      - errors.log: Contains all error messages.
#      - warnings.log: Contains all warning messages.

# 5. **Create a menu-driven application:**
#    - Give the user a list of automation tasks (1-4) and let them choose one to execute. Customize your application by incorporating an additional automation task, choose one:
#      - Counting the number of specific file types in a directory.
#      - Renaming files based on a specific pattern.
#      - Automatically backing up specific folders.
        

if __name__ == "__main__":
  console = Console()