import os
import re

def remove_organize_files():
    for root, dirs, files in os.walk('outputs'):
        for file in files:
            old_path = os.path.join(root, file)

            # Verificar se há resquícios de ordenação no nome do arquivo
            order_match = re.search(r'\d+(\.\d+)?\s', file)
            if order_match:
                # Remover resquícios de ordenação do nome do arquivo
                new_name = re.sub(r'\d+(\.\d+)?\s', '', file).strip()
            else:
                # Se não houver número associado, remover apenas o ponto no início do nome
                new_name = file.lstrip('.')

            # Renomear o arquivo
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

if __name__ == "__main__":
    remove_organize_files()
