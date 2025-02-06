import os
import subprocess
import requests
from appdirs import user_data_dir
from .autounrar import unrar

__all__ = ['unrar']

# Define the directory to store the UnRAR executable
data_dir = user_data_dir("unrar", "unrar_exe")
os.makedirs(data_dir, exist_ok=True)  # Ensure the directory exists

# Path to the UnRAR executable in the data directory
unrar_exe_path = os.path.join(data_dir, "UnRAR.exe")
temp_unrar_installer_path = os.path.join(data_dir, "unrarw64.exe")
license_path = os.path.join(data_dir, "license.txt")

# Check if UnRAR.exe already exists in the data directory
if not os.path.exists(unrar_exe_path):
    # Download the UnRAR installer
    response = requests.get(r"https://www.rarlab.com/rar/unrarw64.exe", stream=True)
    if response.status_code == 200:
        with open(os.path.join(data_dir, "unrarw64.exe"), 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(f"Failed to download UnRAR installer. HTTP status code: {response.status_code}")

    # Run the installer in the data directory
    try:
        subprocess.run([temp_unrar_installer_path, "-s", f"path={data_dir}"], check=True, cwd=data_dir)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to install UnRAR executable: {e}")

    # Clean up the installer file
    if os.path.exists(temp_unrar_installer_path):
        os.remove(temp_unrar_installer_path)

    print("UnRAR executable installed and cleaned up successfully.")
else:
    print("UnRAR executable already exists in the data directory.")