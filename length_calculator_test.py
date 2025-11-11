import pytest
from length_calculator import convert

def test_default_conversion():
    assert convert(1000) == 0.6213727366498067, "Default conversion should be from meters to miles"

def test_specific_conversion():
    assert convert(1000, 1, 4) == 1093.6132983377079, "Should correctly convert from meters to yards"

def test_conversion_with_string_units():
    assert convert(1, to_unit='Inches') == 39.37007874015748, "Should correctly convert to inches when specified with a string"

def test_reverse_conversion():
    assert convert(1, from_unit=2, to_unit=1) == 1609.34, "Should correctly convert from miles to meters"