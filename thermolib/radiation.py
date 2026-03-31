"""Radiative transfer calculations for climate science."""

import numpy as np

from .constants import (
    STANDARD_TEMPERATURE,
    STEFAN_BOLTZMANN_CONSTANT,
)


def calculate_stefan_boltzmann_flux(temperature: float) -> float:
    """
    Calculate outgoing longwave radiation using Stefan-Boltzmann law.

    Fundamental for Earth's energy budget calculations. Uses formula: F = σ*T^4
    where σ is Stefan-Boltzmann constant (5.670374419e-8 W/m²K⁴) and T is temperature
    in Kelvin.

    Parameters
    ----------
    temperature : float
        Temperature in Kelvin (K)

    Returns
    -------
    float
        Radiative flux in watts per square meter (W/m²)

    Raises
    ------
    ValueError
        If temperature is below absolute zero (must be > 0 K)

    Examples
    --------
    >>> olr = calculate_stefan_boltzmann_flux(288.15)
    >>> print(f"Outgoing longwave radiation: {olr:.1f} W/m²")

    References
    ----------
    Stefan-Boltzmann law for blackbody radiation
    https://en.wikipedia.org/wiki/Stefan–Boltzmann_law
    """
    if temperature <= 0:
        error_msg = "Temperature must be above absolute zero"
        raise ValueError(error_msg)

    return STEFAN_BOLTZMANN_CONSTANT * temperature**4


def calculate_earth_energy_balance(
    albedo: float = 0.3,
    solar_constant: float = 1361.0,
) -> float:
    """
    Calculate Earth's effective temperature from energy balance.

    Determines equilibrium temperature from balance between incoming solar radiation
    and outgoing longwave radiation. Uses formula:
    T = [(S(1-A))/(4σ)]^(1/4) where S is solar constant, A is albedo, and σ is
    Stefan-Boltzmann constant.

    Parameters
    ----------
    albedo : float, optional
        Earth's albedo (0-1), fraction of sunlight reflected, default 0.3
    solar_constant : float, optional
        Solar constant in W/m², default 1361 W/m² (current Earth value)

    Returns
    -------
    float
        Effective temperature in Kelvin (K)

    Raises
    ------
    ValueError
        If albedo is outside valid range [0, 1]

    Examples
    --------
    >>> earth_temp = calculate_earth_energy_balance(albedo=0.3)
    >>> print(f"Earth's effective temperature: {earth_temp:.1f} K")

    References
    ----------
    Earth's energy balance and effective radiating temperature
    https://en.wikipedia.org/wiki/Effective_temperature
    """
    if not 0.0 <= albedo <= 1.0:
        error_msg = "Albedo must be between 0 and 1"
        raise ValueError(error_msg)

    return (
        (solar_constant * (1.0 - albedo)) / (4.0 * STEFAN_BOLTZMANN_CONSTANT)
    ) ** 0.25
