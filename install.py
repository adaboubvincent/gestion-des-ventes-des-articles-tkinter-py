def install(module_name: str):
    print(f"Nous n'arrivons pas a acceder au module <<<{module_name}>>>")
    choice = input(f"Installez le module <<<{module_name}>>> y/n [y] : ")
    if choice.strip() == "" or choice.lower() == "y" :
        if module_name == "pysqlite3":
            print("Il se pourrait que l'installation ne serait pas aboutir... Dans ce cas essayez vous meme de l'installer manuellement.")
        print(f"Demarage de l'installation du module <<<{module_name}>>> ")
        import sys
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name])

        print("Running program...")