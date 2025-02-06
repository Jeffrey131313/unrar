import os.path
import subprocess

from appdirs import user_data_dir

data_dir = user_data_dir("unrar", "unrar_exe")
class unrar:
    @staticmethod
    def extract(file_path, to_path=False, password=False):
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        result = subprocess.run(f"{os.path.join(data_dir, "UnRAR.exe")} {"x" if to_path else "e"} {"-p" + password if password else ""} {file_path}{" " + to_path if to_path else ""}", capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def list(path):
        result = subprocess.run(f"{os.path.join(data_dir, "UnRAR.exe")} l {path}",capture_output=True, text=True)
        output = result.stdout

        lines = output.splitlines()
        data = []

        header_line = None
        for i, line in enumerate(lines):
            if line.startswith("-----------"):
                header_line = i
                break

        if header_line is None:
            raise ValueError("Invalid output format: could not find header line.")

        for line in lines[header_line + 1:]:
            if line.startswith("-----------"):
                break

            parts = line.split()
            if len(parts) >= 5:
                attributes = parts[0]
                size = int(parts[1])
                date = parts[2]
                time = parts[3]
                name = " ".join(parts[4:])

                data.append({
                    "attributes": attributes,
                    "size": size,
                    "date": date,
                    "time": time,
                    "name": name
                })

        return data
