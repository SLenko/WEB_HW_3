import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def process_folder(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                extension = os.path.splitext(file)[1][1:]
                destination_folder = os.path.join(folder_path, extension)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(file_path, os.path.join(destination_folder, file))

    except Exception as exception:
        print(f"Error processing folder {folder_path}: {str(exception)}")

def main():
    folder_path = "Хлам"  # Необхідно замінити це на шлях до папки
    thread_count = 4  # Кількість потоків

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.submit(process_folder, folder_path)

if __name__ == "__main__":
    main()
