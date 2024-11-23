import os

def escape_newlines(content):
    """
    Substitui os caracteres de nova linha e retorno de carro por suas representações "\\n" e "\\r".
    """
    return content.replace("\n", "\\n").replace("\r", "\\r")


def merge_files_with_escape(directory_path):
    try:
        # Verifica se o diretório existe
        if not os.path.isdir(directory_path):
            print(f"Error: Directory '{directory_path}' does not exist.")
            return

        # Define o nome do arquivo de saída
        output_file = os.path.basename(directory_path.rstrip(os.sep)) + ".dat"

        with open(output_file, "w", encoding="utf-8") as outfile:
            for file_name in os.listdir(directory_path):
                file_path = os.path.join(directory_path, file_name)

                # Ignorar subdiretórios e apenas processar arquivos
                if os.path.isfile(file_path):
                    try:
                        with open(file_path, "r", encoding="utf-8") as infile:
                            content = infile.read()

                        # Escapar os caracteres de nova linha e retorno de carro
                        escaped_content = escape_newlines(content)

                        # Adicionar o nome do arquivo e o conteúdo ao arquivo de saída
                        outfile.write(f"{file_name}|{escaped_content}\n")
                    except Exception as e:
                        print(f"Could not read file '{file_name}': {e}")

        print(f"Output written to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    directory_path = input("Enter the directory path: ").strip()
    merge_files_with_escape(directory_path)


if __name__ == "__main__":
    main()

