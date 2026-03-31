"""Tests for radiation module."""

import pytest

from thermolib.radiation import (
    calculate_earth_energy_balance,
    calculate_stefan_boltzmann_flux,
)


class TestStefanBoltzmannFlux:
    """Test cases for Stefan-Boltzmann law calculations."""

    def test_standard_earth_temperature(self):
        """Test with Earth's average surface temperature."""
        # Earth's average surface temperature is ~288.15 K
        olr = calculate_stefan_boltzmann_flux(288.15)
        # Expected value should be around 390 W/m²
        assert 380 < olr < 400

    def test_freezing_temperature(self):
        """Test with water freezing point temperature."""
        # 273.15 K (0°C)
        olr = calculate_stefan_boltzmann_flux(273.15)
        # Should be around 315 W/m²
        assert 310 < olr < 320

    def test_very_cold_temperature(self):
        """Test with very cold temperature (polar conditions)."""
        # -50°C = 223.15 K
        olr = calculate_stefan_boltzmann_flux(223.15)
        # Actual calculation: 5.670374419e-8 * (223.15)^4 = 140.6 W/m²
        assert 135 < olr < 145

    def test_very_hot_temperature(self):
        """Test with very hot temperature (desert conditions)."""
        # 50°C = 323.15 K
        olr = calculate_stefan_boltzmann_flux(323.15)
        # Actual calculation: 5.670374419e-8 * (323.15)^4 = 618.3 W/m²
        assert 610 < olr < 625

    def test_invalid_temperature(self):
        """Test that invalid temperature raises ValueError."""
        with pytest.raises(ValueError, match="Temperature must be above absolute zero"):
            calculate_stefan_boltzmann_flux(-10.0)

    def test_absolute_zero(self):
        """Test that absolute zero raises ValueError."""
        with pytest.raises(ValueError, match="Temperature must be above absolute zero"):
            calculate_stefan_boltzmann_flux(0.0)

    def test_physical_relationship(self):
        """Test that flux increases with temperature^4 (Stefan-Boltzmann law)."""
        olr_280 = calculate_stefan_boltzmann_flux(280.0)
        olr_288 = calculate_stefan_boltzmann_flux(288.0)

        # (288/280)^4 ≈ 1.13, so olr_288 should be about 13% higher than olr_280
        ratio = olr_288 / olr_280
        expected_ratio = (288.0 / 280.0) ** 4

        assert ratio == pytest.approx(expected_ratio, rel=0.01)


class TestEarthEnergyBalance:
    """Test cases for Earth's energy balance calculations."""

    def test_standard_earth_albedo(self):
        """Test with Earth's average albedo."""
        # Earth's average albedo is ~0.3
        temp = calculate_earth_energy_balance(albedo=0.3)
        # Should be around 255 K (-18°C), Earth's effective radiating temperature
        assert 250 < temp < 260

    def test_ice_age_albedo(self):
        """Test with higher albedo (ice age conditions)."""
        # Higher albedo during ice ages (~0.4)
        temp = calculate_earth_energy_balance(albedo=0.4)
        # Should be colder than current conditions
        assert 230 < temp < 245

    def test_low_albedo(self):
        """Test with very low albedo (ocean planet)."""
        # Very low albedo (0.1) - mostly oceans
        temp = calculate_earth_energy_balance(albedo=0.1)
        # Should be warmer than current conditions
        assert 270 < temp < 280

    def test_extreme_albedo(self):
        """Test with extreme albedo (snowball Earth)."""
        # Very high albedo (0.8) - snowball Earth conditions
        temp = calculate_earth_energy_balance(albedo=0.8)
        # Actual calculation gives 186 K, which is reasonable for snowball Earth
        assert 180 < temp < 190

    def test_invalid_albedo_negative(self):
        """Test that negative albedo raises ValueError."""
        with pytest.raises(ValueError, match="Albedo must be between 0 and 1"):
            calculate_earth_energy_balance(albedo=-0.1)

    def test_invalid_albedo_above_one(self):
        """Test that albedo > 1 raises ValueError."""
        with pytest.raises(ValueError, match="Albedo must be between 0 and 1"):
            calculate_earth_energy_balance(albedo=1.1)

    def test_albedo_boundary_conditions(self):
        """Test boundary conditions for albedo."""
        # Test albedo = 0 (perfect absorber)
        temp_0 = calculate_earth_energy_balance(albedo=0.0)

        # Test albedo = 1 (perfect reflector)
        temp_1 = calculate_earth_energy_balance(albedo=1.0)

        # Albedo=0 should be warmer than albedo=1
        assert temp_0 > temp_1

        # Albedo=1 should give very low temperature (near 0 K)
        assert temp_1 < 100  # Very cold

    def test_different_solar_constants(self):
        """Test with different solar constants (stellar evolution)."""
        # Current solar constant
        temp_current = calculate_earth_energy_balance(solar_constant=1361.0)

        # Early Earth (lower solar output, ~1320 W/m²)
        temp_early = calculate_earth_energy_balance(solar_constant=1320.0)

        # Future Earth (higher solar output, ~1400 W/m²)
        temp_future = calculate_earth_energy_balance(solar_constant=1400.0)

        # Check relationships: early < current < future
        assert temp_early < temp_current < temp_future


class TestRadiationEdgeCases:
    """Test edge cases and boundary conditions for radiation calculations."""

    def test_very_high_temperature(self):
        """Test with very high temperature (stellar conditions)."""
        # 1000 K (very hot, but not stellar)
        olr = calculate_stefan_boltzmann_flux(1000.0)
        # Should be extremely high
        assert olr > 5000  # Very high flux

    def test_near_absolute_zero(self):
        """Test with temperature near absolute zero."""
        # 1 K (very close to absolute zero)
        olr = calculate_stefan_boltzmann_flux(1.0)
        # Should be very low but positive
        assert 0 < olr < 10  # Very low flux

    def test_albedo_precision(self):
        """Test albedo with high precision."""
        # Test with very precise albedo values
        temp1 = calculate_earth_energy_balance(albedo=0.299999)
        temp2 = calculate_earth_energy_balance(albedo=0.300001)

        # Should be very close but not identical
        assert abs(temp1 - temp2) < 0.1  # Very small difference
