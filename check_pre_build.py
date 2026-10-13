import subprocess
import sys


def run_check(command, description):
    print(f"\n[+] Ejecutando: {description}...")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"\n❌ Error en el paso: {description}.")
        print("Corrige los errores indicados antes de proceder a la compilación.")
        sys.exit(1)
    print(f"✓ {description} completado con éxito.")


def main():
    print("==========================================")
    print(" INICIANDO COMPROBACIÓN PREVIA A COMPILAR ")
    print("==========================================")

    # 1. Flake8
    run_check("flake8 src/", "Análisis de sintaxis y estilo (Flake8)")

    # 2. Pylint con flags directos para evitar falsos positivos con Flet
    pylint_cmd = (
        "pylint "
        "--disable=unexpected-keyword-arg,no-value-for-parameter,"
        "too-many-function-args,no-member,missing-module-docstring,"
        "missing-class-docstring,missing-function-docstring,"
        "broad-exception-caught,unused-argument,too-many-instance-attributes,"
        "not-callable "
        "src/"
    )
    run_check(pylint_cmd, "Análisis profundo de código (Pylint)")

    # 3. Mypy
    run_check("mypy src/", "Verificación de tipos (Mypy)")

    # 4. Pytest
    run_check("pytest", "Ejecución de Pruebas Unitarias (Pytest)")

    print("\n==========================================")
    print(" 🎉 TODAS LAS PRUEBAS PASARON CORRECTAMENTE")
    print(" El proyecto está listo para ser compilado.")
    print("==========================================")


if __name__ == "__main__":
    main()
