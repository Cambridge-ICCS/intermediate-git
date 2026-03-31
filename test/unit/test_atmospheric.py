"""Tests for atmospheric module."""

import pytest

from thermolib.atmospheric import (
    calculate_air_density,
)


class TestAirDensity:
    """Test cases for air density calculations."""

    def test_standard_conditions(self):
        """Test air density at standard atmospheric conditions."""
        # Standard conditions: 101325 Pa, 288.15 K
        density = calculate_air_density(101325.0, 288.15)
        expected = 1.225  # Standard air density at sea level
        assert density == pytest.approx(expected, rel=0.01)

    def test_high_altitude(self):
        """Test air density at high altitude (low pressure)."""
        # At ~5000m, pressure ~54000 Pa, temp ~255.7 K
        density = calculate_air_density(54000.0, 255.7)
        expected = 0.736  # Expected density at 5000m
        assert density == pytest.approx(expected, rel=0.01)

    def test_invalid_pressure(self):
        """Test that invalid pressure raises ValueError."""
        with pytest.raises(ValueError, match="Pressure must be positive"):
            calculate_air_density(-1000.0, 288.15)

    def test_invalid_temperature(self):
        """Test that invalid temperature raises ValueError."""
        with pytest.raises(ValueError, match="Temperature must be positive"):
            calculate_air_density(101325.0, -10.0)
