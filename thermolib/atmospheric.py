"""Atmospheric thermodynamic calculations for climate science."""

import numpy as np

from .constants import (
    GRAVITATIONAL_ACCELERATION,
    SPECIFIC_GAS_CONSTANT_DRY_AIR,
    SPECIFIC_HEAT_CAPACITY_DRY_AIR,
    STANDARD_ATMOSPHERIC_PRESSURE,
)


def calculate_air_density(pressure: float, temperature: float) -> float:
    """
    Calculate air density using ideal gas law.

    Fundamental for atmospheric calculations in climate models.
    Computes air density based on the ideal gas law:
    density = pressure / (specific_gas_constant * temperature).

    Parameters
    ----------
    pressure : float
        Air pressure in Pascals (Pa)
    temperature : float
        Air temperature in Kelvin (K)

    Returns
    -------
    float
        Air density in kilograms per cubic meter (kg/m³)

    Raises
    ------
    ValueError
        If pressure or temperature values are unrealistic for atmospheric conditions

    Examples
    --------
    >>> density = calculate_air_density(101325.0, 288.15)
    >>> print(f"Air density: {density:.3f} kg/m³")

    References
    ----------
    Standard atmospheric calculations based on ideal gas law
    https://en.wikipedia.org/wiki/Density_of_air
    """
    if pressure <= 0:
        error_msg = "Pressure must be positive for atmospheric calculations"
        raise ValueError(error_msg)
    if temperature <= 0:
        error_msg = "Temperature must be positive for atmospheric calculations"
        raise ValueError(error_msg)

    return pressure / (SPECIFIC_GAS_CONSTANT_DRY_AIR * temperature)


# --------- Add functions during the git workshop here ---------

def hydrostatic_pressure(pressure: float, temperature: float, height: float) -> float:
    #Calculate hydrostatic pressure
    return pressure * np.exp((-GRAVITATIONAL_ACCELERATION*height)/(temperature*SPECIFIC_GAS_CONSTANT_DRY_AIR))
# --------------------------------------------------------------