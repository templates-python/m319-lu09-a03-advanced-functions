"""Unit tests for the main module."""

import pytest
from main import div


def test_division_normal():
    assert div(34, 6) == (5, 4), 'Should return (5, 4) for div(34, 6)'


def test_division_zero_remainder():
    assert div(50, 5) == (10, 0), 'Should return (10, 0) for div(50, 5)'


def test_division_by_zero():
    assert div(34, 0) is None, 'Should return None for div(34, 0)'
