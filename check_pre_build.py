import subprocess
import sys


def run_check(command, step_name):
    print(f"\n[+] Ejecutando: {step_name}...")
    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        print(f"\n❌ Error en el paso: {step_name}.")
        print("Corrige los errores indicados antes de proceder a la compilación.")
        sys.exit(1)
    else:
        print(f"✓ {step_name} completado con éxito.")


def main():
    print("==========================================")
    print(" INICIANDO COMPROBACIÓN PREVIA A COMPILAR ")
    print("==========================================")

    # 1. Verificación sintáctica y estilo con Flake8
    run_check("flake8 src/", "Análisis de sintaxis y estilo (Flake8)")

    # 2. Análisis estático de código con Pylint
    run_check("pylint src/", "Análisis profundo de código (Pylint)")

    # 3. Verificación de tipos estáticos con Mypy
    run_check("mypy src/", "Verificación de tipos (Mypy)")

    # 4. Pruebas unitarias automatizadas con Pytest
    run_check("pytest tests/", "Ejecución de Pruebas Unitarias (Pytest)")

    print("\n==========================================")
    print(" 🎉 TODAS LAS PRUEBAS PASARON CORRECTAMENTE ")
    print(" El proyecto está listo para ser compilado. ")
    print("==========================================")


if __name__ == "__main__":
    main()