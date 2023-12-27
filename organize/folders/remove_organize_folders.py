import os
import re

def remove_organize_folders():
    outputs_path = 'outputs'

    # Listar todas as pastas em ordem alfabética
    folders = sorted(os.listdir(outputs_path))

    for folder_name in folders:
        old_path = os.path.join(outputs_path, folder_name)

        # Remover números e espaços adicionados
        new_folder_name = re.sub(r'^\d+\s', '', folder_name)

        # Renomear a pasta
        new_path = os.path.join(outputs_path, new_folder_name)
        os.rename(old_path, new_path)

if __name__ == "__main__":
    remove_organize_folders()
