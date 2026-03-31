"""Moisture calculations for atmospheric science."""

import numpy as np


def calculate_saturation_vapor_pressure(temperature: float) -> float:
    """
    Calculate saturation vapor pressure over liquid and ice.

    Parameters
    ----------
    temperature: float
        Temperature in Kelvin (K)

    Returns
    -------
    float
        Saturation vapor pressure in Pascals (Pa)

    Raises
    ------
    ValueError
        If temperature is below absolute zero

    References
    ----------
    Bolton 1980
    Guide to Meteorological Instruments and Methods of Observation (2008)
    See https://www.eol.ucar.edu/data-software/conventions-and-standards/water-vapor-pressure-formulations

    Examples
    --------
    >>> svp = calculate_saturation_vapor_pressure(298.15)
    >>> print(f"Saturation vapor pressure: {svp:.1f} Pa")
    """
    if temperature <= 0:
        error_msg = "Temperature must be above absolute zero"
        raise ValueError(error_msg)

    # Convert to Celsius for the empirical formula
    temp_c = temperature - 273.15

    if temp_c < 0:  # Below freezing (ice)
        return 611.2 * np.exp(22.46 * temp_c / (temp_c + 272.6))
    else:  # Above freezing (water)
        return 611.2 * np.exp(17.67 * temp_c / (temp_c + 243.5))
