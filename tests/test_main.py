import sys
from pathlib import Path
import pytest
from datetime import date

# Asegura que la raíz del proyecto esté en el path de búsqueda
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.main import parse_fecha


def test_parse_fecha_valida():
    """Verifica que el formateador parsea correctamente fechas válidas."""
    assert parse_fecha("15/10/2026") == date(2026, 10, 15)
    assert parse_fecha("01/01/25") == date(2025, 1, 1)
    assert parse_fecha("2026-12-31") == date(2026, 12, 31)


def test_parse_fecha_invalida():
    """Verifica que se lance ValueError ante formatos incorrectos."""
    with pytest.raises(ValueError):
        parse_fecha("fecha-invalida")
