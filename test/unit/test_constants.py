"""Test cases for constants module."""

import pytest

from thermolib.constants import (
    GRAVITATIONAL_ACCELERATION,
    SPECIFIC_GAS_CONSTANT_DRY_AIR,
    SPECIFIC_HEAT_CAPACITY_DRY_AIR,
    STANDARD_ATMOSPHERIC_PRESSURE,
    STEFAN_BOLTZMANN_CONSTANT,
    UNIVERSAL_GAS_CONSTANT,
)


class TestConstantsValues:
    """Test that constants have expected values."""

    def test_universal_gas_constant(self):
        """Test universal gas constant value."""
        # Expected value: 8.31446261815324 J/(mol·K)
        assert abs(UNIVERSAL_GAS_CONSTANT - 8.314462618) < 1e-9

    def test_specific_gas_constant_dry_air(self):
        """Test specific gas constant for dry air."""
        # Expected value: 287.058 J/(kg·K)
        assert abs(SPECIFIC_GAS_CONSTANT_DRY_AIR - 287.058) < 1e-3

    def test_specific_heat_capacity_dry_air(self):
        """Test specific heat capacity for dry air."""
        # Expected value: 1005.0 J/(kg·K)
        assert abs(SPECIFIC_HEAT_CAPACITY_DRY_AIR - 1005.0) < 1e-3

    def test_standard_atmospheric_pressure(self):
        """Test standard atmospheric pressure."""
        # Expected value: 101325 Pa
        assert STANDARD_ATMOSPHERIC_PRESSURE == 101325.0

    def test_stefan_boltzmann_constant(self):
        """Test Stefan-Boltzmann constant."""
        # Expected value: 5.670374419e-8 W/(m²·K⁴)
        assert abs(STEFAN_BOLTZMANN_CONSTANT - 5.670374419e-8) < 1e-15

    def test_gravitational_acceleration(self):
        """Test gravitational acceleration."""
        # Expected value: 9.80665 m/s² (standard gravity)
        assert abs(GRAVITATIONAL_ACCELERATION - 9.80665) < 1e-5


class TestConstantsTypes:
    """Test that constants have correct types."""

    def test_all_constants_are_numeric(self):
        """Test that all constants are numeric values."""
        constants = [
            UNIVERSAL_GAS_CONSTANT,
            SPECIFIC_GAS_CONSTANT_DRY_AIR,
            STANDARD_ATMOSPHERIC_PRESSURE,
            STEFAN_BOLTZMANN_CONSTANT,
            GRAVITATIONAL_ACCELERATION,
        ]

        for constant in constants:
            assert isinstance(constant, (int, float))
            assert not isinstance(constant, bool)  # Ensure not boolean

    def test_constants_are_positive(self):
        """Test that physical constants are positive."""
        constants = [
            UNIVERSAL_GAS_CONSTANT,
            SPECIFIC_GAS_CONSTANT_DRY_AIR,
            STANDARD_ATMOSPHERIC_PRESSURE,
            STEFAN_BOLTZMANN_CONSTANT,
            GRAVITATIONAL_ACCELERATION,
        ]

        for constant in constants:
            assert constant > 0
