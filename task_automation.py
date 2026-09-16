from pathlib import Path
import shutil


def organize_jpg_files():
    source_folder = Path(input("Enter the folder containing JPG files: ").strip())

    if not source_folder.exists() or not source_folder.is_dir():
        print("Folder does not exist.")
        return

    destination_folder = source_folder / "JPG_Files"
    destination_folder.mkdir(exist_ok=True)

    moved = 0

    for file in source_folder.iterdir():
        if file.is_file() and file.suffix.lower() == ".jpg":
            destination = destination_folder / file.name

            # Avoid overwriting an existing file.
            counter = 1
            while destination.exists():
                destination = destination_folder / f"{file.stem}_{counter}{file.suffix}"
                counter += 1

            shutil.move(str(file), str(destination))
            moved += 1

    print(f"Automation completed. {moved} JPG file(s) moved to '{destination_folder}'.")


if __name__ == "__main__":
    organize_jpg_files()
