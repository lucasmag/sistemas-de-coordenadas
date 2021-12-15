## Computação gráfica
### Sistema de coordenadas

A presente aplicação se trata da geração de sólidos em diferentes sistemas. São eles o do objeto, do mundo, e da câmera. 

Para rodar o projeto certifique-se que o python está instalado na máquina (python>=3.6).
```bash
$ python --version
Python 3.8.10
```

Instale o gerenciador de ambientes virtuais [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):
```bash
$ sudo apt install python3-virtualenv
```

Crie um ambiente virtual:
```bash
$ virtualenv venv
```

Ative o ambiente virtual:
```bash
$ source venv/bin/activate
```

Instale as dependêcias:
```bash
$ pip install -r requirements.txt
```

---

Para rodar a aplicação, execute o arquivo `main.py` seguido da flag referente ao módulo a ser executado.

Por exemplo, para plotar o Cubo, basta rodar o comando:

```bash
$ python main.py --cubo
```

Lista de flags disponíveis:

```bash
--help, -h, mostra ajuda
--cubo, -c, Cria cubo no matplotlib
--paralelepipedo, -r, Cria paralelepipedo no matplotlib
--piramide, -p, Cria piramide no matplotlib
--tronco, -t, Cria tronco no matplotlib
--mundo, -m, Cria mundo no matplotlib
--camera, -k, Cria visao de camera no pyopengl
```

Flags opcionais para serem usadas na visão de câmera:
```bash
--ortogonal, -o, Aplica visao ortogonal na opção de camera
--terceira_pessoa, Mostra elementos da cena na opção de camera
--so_arestas, Mostra somente arestas dos objetos na opção de camera
```

Para aplicar visao ortogonal, por exemplo, basta rodar o comando:
```bash
$ python main.py --camera --ortogonal
```