import os
import re

def organize_music():
    deleting_names = ['GTA V Radio [Channel X]', 'GTA V - Rebel Radio', 'GTA V Radio [FLyLo FM]', 'GTA V [Radio Mirror Park]']

    for root, dirs, files in os.walk('outputs'):
        # Ordenar os arquivos para garantir a ordem correta
        files.sort()

        folder_name = os.path.basename(root)
        order_number = folder_name.split('.')[0]

        for file_index, file in enumerate(files, start=1):
            old_path = os.path.join(root, file)

            # Remover palavras-chave do nome do arquivo
            new_name = file
            for name in deleting_names:
                new_name = new_name.replace(name, '')

            # Verificar se a numeração já está presente
            existing_order_match = re.search(r'^\d+\.\d+', new_name)
            if existing_order_match:
                new_name = re.sub(r'^\d+\.\d+', f"{order_number}.{existing_order_match.group(0).split('.')[1]}", new_name)
            else:
                # Adicionar ordem nas músicas
                new_name = f"{order_number}.{file_index} {new_name}"

            # Renomear o arquivo
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

if __name__ == "__main__":
    organize_music()
