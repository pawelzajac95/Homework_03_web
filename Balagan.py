import os
import shutil
from concurrent.futures import ThreadPoolExecutor


def sort_files_by_extension(source_folder, destination_folder):
    # Tworzenie listy plików w folderze źródłowym
    files_to_move = []
    for root, _, files in os.walk(source_folder):
        for file in files:
            files_to_move.append(
                (os.path.join(root, file), os.path.join(destination_folder, file)))

    # Definicja funkcji do przenoszenia plików
    def move_file(src, dst):
        shutil.move(src, dst)

    # Utworzenie puli wątków i przetwarzanie plików
    with ThreadPoolExecutor(max_workers=5) as executor:
        for src, dst in files_to_move:
            executor.submit(move_file, src, dst)


if __name__ == "__main__":
    source_folder = "Bałagan"
    destination_folder = "Posortowane"

    # Upewnij się, że folder docelowy istnieje
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    sort_files_by_extension(source_folder, destination_folder)
