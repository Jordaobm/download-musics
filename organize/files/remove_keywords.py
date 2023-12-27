import os
import re

def remove_keywords():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    outputs_path = os.path.join(script_directory, '..', '..', 'outputs')

    keywords_to_remove = ['Alphaville - ']


    for root, dirs, files in os.walk(outputs_path):
        # Ordenar os arquivos para garantir a ordem correta
        files.sort()

        for file in files:
            old_path = os.path.join(root, file)

            # Remover palavras-chave do nome do arquivo
            new_name = file
            for name in keywords_to_remove:
                new_name = new_name.replace(name, '')

            # Remover espaços em branco no início e no final do nome
            new_name = new_name.strip()

            # Ajustar espaços em branco entre a ordem e o nome
            new_name = re.sub(r'(?<=\d)\s+', ' ', new_name)

            # Renomear o arquivo
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

if __name__ == "__main__":
    remove_keywords()
