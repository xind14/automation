from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
import re
import shutil




def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        console.print(f"[red]folder '{folder_name}' created successfully.[red]")
    except FileExistsError:
        console.print(f"[red]Folder '{folder_name}' already exists.[red]")




# Example usage:

# 2. **Handle a deleted user:**
#    - User2 is a deleted user and needs to move their documents from their user folder to a temporary folder. Your script will create the temporary folder. This will effectively delete the user from the system while still maintaining a record of their documents.

# 3. **Sort documents into appropriate folders:**
#    - Go through a given folder and sort the documents into additional folders based on their file type.
#      - Move log files into a logs folder. If a logs folder doesn’t exist, your script should create one.
#      - Move email files into a mail folder. If a mail folder doesn’t exist, your script should create one.

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