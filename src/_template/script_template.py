"""
Template para novos scripts do projeto.

Como usar:
- Copie este arquivo para outro lugar (por ex.: src/p1_et1.py)
- Renomeie funções, docstring e implemente a lógica específica.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    """
    Ponto de entrada principal da etapa.
    Implemente aqui a lógica de ETL/modelo/etc.
    """
    print("[template] Script criado a partir de src/_template/script_template.py")
    # TODO: adicionar código da etapa


if __name__ == "__main__":
    main()
