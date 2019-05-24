import os

def walk(diretorio):
    """Printa todos os arquivos de um dado diretorio assim como de seus subdiretorios.

    diretorio: nome de string do  diretorio
    """
    for name in os.listdir(diretorio):
        path = os.path.join(diretorio, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

if __name__ == '__main__':
    walk('.')

