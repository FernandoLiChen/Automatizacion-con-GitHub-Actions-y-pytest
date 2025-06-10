import pytest
from area_triangulo import calcular_area_triangulo

def test_area_triangulo_valores_positivos():
    """Test para validar el cálculo del área con valores positivos"""
    base = 5
    altura = 7
    area_esperada = 17.5 
    assert calcular_area_triangulo(base, altura) == area_esperada

def test_area_triangulo_valores_negativos():
    """Test para validar que no se acepten valores negativos"""
    assert calcular_area_triangulo(-5, 7) == False
    assert calcular_area_triangulo(5, -7) == False

def test_area_triangulo_base_cero():
    """Test para validar que la base no sea cero"""
    assert calcular_area_triangulo(0, 7) == False
