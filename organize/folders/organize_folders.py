import os

def organize_folders():
    outputs_path = 'outputs'

    # Listar todas as pastas em ordem alfabética
    folders = sorted(os.listdir(outputs_path))

    for folder_index, folder_name in enumerate(folders, start=1):
        old_path = os.path.join(outputs_path, folder_name)

        # Formatar o novo nome da pasta com ordem numerada
        new_folder_name = f"{folder_index:02}. {folder_name}"

        # Renomear a pasta
        new_path = os.path.join(outputs_path, new_folder_name)
        os.rename(old_path, new_path)

if __name__ == "__main__":
    organize_folders()
