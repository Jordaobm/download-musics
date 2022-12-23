# Download de músicas

Destinado ao uso pessoal apenas para download de músicas diretamente do YouTube, o código foi desenvolvido em Python utilizando **pytube** e **typer**. **pytube** foi utilizado para realizar o download dos arquivos e **typer** foi utilizado para executar o comando fornecido. 

Para baixar as músicas primeiro clone o repositório usando:

    git clone https://github.com/Jordaobm/download-musics.git
    cd download-musics


Em seguida, instale o [Python](https://www.python.org/downloads/) em sua máquina caso não tenha.
Agora, basta preencher o arquivo **musics.txt** com os links que você deseja baixar, colocando cada um em uma linha.

Execute o comando abaixo em um terminal partindo de dentro do repositório e aguarde;

    python get-yt.py

Suas músicas serão baixadas dentro de ./outputs/
