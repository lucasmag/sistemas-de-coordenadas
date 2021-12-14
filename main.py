import argparse

from solidos.cubo import criar_cubo
from solidos.paralelepipedo import criar_paralelepipedo
from solidos.piramide import criar_piramide
from solidos.tronco import criar_tronco
from mundo import criar_mundo
from camera import criar_camera


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cubo", "-c", action='store_true', help="Cria cubo no matplotlib")
    parser.add_argument("--paralelepipedo", "-r", action='store_true', help="Cria paralelepipedo no matplotlib")
    parser.add_argument("--piramide", "-p", action='store_true', help="Cria piramide no matplotlib")
    parser.add_argument("--tronco", "-t", action='store_true', help="Cria tronco no matplotlib")
    parser.add_argument("--mundo", "-m", action='store_true', help="Cria mundo no matplotlib")
    parser.add_argument("--camera", "-k", action='store_true', help="Cria visao de camera no pyopengl")
    parser.add_argument("--ortogonal", "-o", action='store_true', help="Aplica visao ortogonal na visão de camera")
    parser.add_argument("--terceira_pessoa", action='store_true', help="Mostra posicao da camera na visao de camera")
    parser.add_argument("--so_arestas", action='store_true', help="Mostra somente arestas dos objetos na visao de camera (exceto ortogonal)")

    return parser.parse_args()


def main():
    args = parse()

    if not args.camera and any([args.so_arestas, args.ortogonal, args.terceira_pessoa]):
        print("Aviso: As opções --ortogonal, --terceira_pessoa e --so_arestas só farão efeito junto à flag --camera.")

    if args.cubo:
        criar_cubo()
    elif args.paralelepipedo:
        criar_paralelepipedo()
    elif args.piramide:
        criar_piramide()
    elif args.tronco:
        criar_tronco()
    elif args.mundo:
        criar_mundo()
    elif args.camera:
        criar_camera(args.so_arestas, args.ortogonal, args.terceira_pessoa)
    else:
        print("Opção não reconhecida")


if __name__ == "__main__":
    main()
