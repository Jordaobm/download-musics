import os
import re

def organize_music():
    deleting_names = ['GTA V Radio [Channel X]', 'GTA V - Rebel Radio', 'GTA V Radio [FLyLo FM]', 'GTA V [Radio Mirror Park]']

    for root, dirs, files in os.walk('outputs'):
        for file_index, file in enumerate(files, start=1):
            old_path = os.path.join(root, file)

            # Remover palavras-chave do nome do arquivo
            new_name = file
            for name in deleting_names:
                new_name = new_name.replace(name, '')

            # Adicionar ordem nas músicas apenas se não houver ordenação existente
            if not re.match(r'^\d+\.\d+', new_name):
                folder_name = os.path.basename(root)
                order_number = folder_name.split('.')[0]
                new_name = f"{order_number}.{file_index} {new_name}"

                # Renomear o arquivo
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)

if __name__ == "__main__":
    organize_music()
