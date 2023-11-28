# Download de músicas

Destinado ao uso pessoal apenas para download de músicas diretamente do YouTube, o código foi desenvolvido em Python utilizando **pytube** e **typer**. **pytube** foi utilizado para realizar o download dos arquivos e **typer** foi utilizado para executar o comando fornecido.

## Como usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/Jordaobm/download-musics.git
   cd download-musics
   ```

2. Certifique-se de ter o Python instalado no seu computador.

3. Abra um terminal PowerShell na raiz do projeto e execute os seguintes comandos:

   ```bash
   # Cria o ambiente virtual do Python
   python -m venv venv

   # Ativa o ambiente virtual do Python
   venv\Scripts\activate

   # Instala as dependências do projeto
   pip install -r .\requirements.txt

   # Executa o código, baixando as músicas presentes dentro de musics.txt
   python .\get-yt.py
   ```

Suas músicas serão baixadas dentro de `./outputs/`.
