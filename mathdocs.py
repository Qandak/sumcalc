# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


from PyQt5.QtCore import QT_TRANSLATE_NOOP


errors = {
        'oiv': QT_TRANSLATE_NOOP('MathErrors',
                                 'only accepts integral values.'),
        'oivDig': QT_TRANSLATE_NOOP('MathErrors',
                                 'only accepts integral values for digits count.'),
        'nv': QT_TRANSLATE_NOOP('MathErrors',
                                 'not defined for negative values.'),
        'mde': QT_TRANSLATE_NOOP('MathErrors',
                                'math domain error'),
        'fac64': QT_TRANSLATE_NOOP('MathErrors',
                                'calculations limited by <b>64</b>.'),
    }


docs = {
        'sum': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the Sum of all arguments.'),
        'mod': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the remainder after division.'),
        'ceil': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the ceiling of <b>x</b>.'),
        'exp': QT_TRANSLATE_NOOP('Mathdocs',
                'returns <b>e</b> raised to the power <b>x</b>.'),
        'fact': QT_TRANSLATE_NOOP('Mathdocs',
                'returns <b>n</b> factorial.'),
        'sqrt': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the square root of <b>x</b>.'),
        'floor': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the floor of <b>x</b>.'),
        'pow': QT_TRANSLATE_NOOP('Mathdocs',
                'returns <b>x</b> raised to the power <b>y</b>.'),
        'deg': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Radians to Degrees.'),
        'rad': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Degrees to Radians.'),
        'hyp': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the Euclidean norm, '
                'the length of the vector from the origin to point (<b>x</b>, <b>y</b>).'),
        'log10': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the base-10 logarithm of <b>x</b>.'),
        'log2': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the base-2 logarithm of <b>x</b>.'),
        # Extending LOGARITHMIC function
        'log': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the logarithm of <b>x</b> to the <b>y</b> base.'),
        'lg': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the base-10 logarithm of <b>x</b>.'),
        'ln': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the natural logarithm of <b>x</b> (to base <b>e</b>).'),

        # Redefining TRIGONOMETRIC functions to switch betweeen Degrees and Radians

        'acosh': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the inverse hyperbolic cosine of <b>x</b>.'),
        'asinh': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the inverse hyperbolic sine of <b>x</b>.'),
        'atanh': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the inverse hyperbolic tangent of <b>x</b>.'),
        'cosh': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the hyperbolic cosine of <b>x</b>.'),
        'sinh': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the hyperbolic sine of <b>x</b>.'),
        'tanh': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the hyperbolic tangent of <b>x</b>.'),
        'acos': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the arc cosine of <b>x</b> in radians or degrees.'),
        'asin': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the arc sine of <b>x</b> in radians or degrees.'),
        'atan': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the arc tangent of <b>x</b> in radians or degrees.'),
        'atan2': QT_TRANSLATE_NOOP('Mathdocs',
                'returns atan(<b>y</b> / <b>x</b>) in radians or degrees.'),
        'cos': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the cosine of <b>x</b> angle (in radians or degrees).'),
        'sin': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the sine of <b>x</b> angle (in radians or degrees).'),
        'tan': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the tangent of <b>x</b> angle (in radians or degrees).'),

        # Special functions

        'erf': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the error function at <b>x</b>.'),
        'erfc': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the complementary error function at <b>x</b>.'),
        'gamma': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the Gamma function at <b>x</b>.'),
        'lgamma': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the natural logarithm of the absolute value '
                'of the Gamma function at <b>x</b>.'),
        'cdf': QT_TRANSLATE_NOOP('Mathdocs',
                'returns cumulative distribution function (CDF) '
                'for the standard normal distribution.'),

        # Redefining BUILTIN functions

        'bin': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the binary representation of <b>x</b>.'),
        'oct': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the octal representation of <b>x</b>.'),
        'hex': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the hexadecimal representation of <b>x</b>.'),
        'round': QT_TRANSLATE_NOOP('Mathdocs',
                'if <i>dig</i> is omitted, returns the nearest integer of <b>x</b>, '
                'otherwise - rounded to <i>dig</i> (digits) after point.'),
        'abs': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the absolute value of <b>x</b>.'),
        'min': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the smallest item in arguments list.'),
        'max': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the largest item in arguments list.'),

        # USER-DEFINED Functions

        'rt': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the <b>Nth</b> root of <b>x</b>.'),
        'cbrt': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the cube root of <b>x</b>.'),
        'pc': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the <b>percent</b> of <b>x</b> (see also <b>perc</b> function).'),
        'perc': QT_TRANSLATE_NOOP('Mathdocs',
                'returns <b>x</b> increased or (-) decreased by <b>percent</b> (see also <b>pc</b> function).'),
        'dperc': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the percentage change from <b>old</b> to <b>new</b> numbers.'),
        'gcd': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the Greatest Common Divisor (GCD) of <b>x</b> and <b>y</b>.'),
        'dms': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Degrees(°), Minutes(\'), Seconds(\") to decimal value.'),
        'dd': QT_TRANSLATE_NOOP('Mathdocs',
                'converts degrees in decimal value to Degrees(°), Minutes(\'), Seconds(\").'),
        'amn': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the Arithmetic Mean (average) of all arguments.'),
        'gmn': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the Geometric Mean of all arguments.'),
        'hmn': QT_TRANSLATE_NOOP('Mathdocs',
                'returns the Harmonic Mean of all arguments.'),

        # CONVERSION Functions

        # Length

        'in_mm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Inch to Millimeter.'),
        'in_cm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Inch to Centimeter.'),
        'in_m': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Inch to Meter.'),
        'ft_in': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Foot to Inch.'),
        'ft_mm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Foot to Millimeter.'),
        'ft_cm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Foot to Centimeter.'),
        'ft_m': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Foot to Meter.'),
        'ftin_cm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Foot and Inches to Centimeter.'),
        'ftin_m': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Foot and Inches to Meter.'),
        'yd_in': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Yard to Inch.'),
        'yd_ft': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Yard to Foot.'),
        'yd_mm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Yard to Millimeter.'),
        'yd_cm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Yard to Centimeter.'),
        'yd_m': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Yard to Meter.'),
        'yd_km': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Yard to Kilometer.'),
        'mi_yd': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Mile to Yard.'),
        'mi_m': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Mile to Meter.'),
        'mi_km': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Mile to Kilometer.'),

        'mm_in': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Millimeter to Inch.'),
        'cm_in': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Centimeter to Inch.'),
        'cm_ft': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Centimeter to Foot.'),
        'cm_ftin': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Centimeter to Foot and Inches.'),
        'm_in': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Meter to Inch.'),
        'm_ft': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Meter to Foot.'),
        'm_ftin': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Meter to Foot and Inches.'),
        'm_yd': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Meter to Yard.'),
        'm_mi': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Meter to Mile.'),
        'km_mi': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Kilometer to Mile.'),

        # Area

        'sqcm_sqin': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Centimeter to Square Inch.'),
        'sqm_sqft': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Meter to Square Foot.'),
        'sqm_sqyd': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Meter to Square Yard.'),
        'sqm_ac': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Meter to Acre.'),
        'sqm_ha': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Meter to Hectare.'),
        'sqkm_sqmi': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Kilometer to Square Mile.'),
        'sqin_sqcm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Inch to Square Centimeter.'),
        'sqft_sqm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Foot to Square Meter.'),
        'sqyd_sqm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Yard to Square Meter.'),
        'sqmi_sqkm': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Mile to Square Kilometer.'),
        'sqmi_ac': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Mile to Acre.'),
        'sqmi_ha': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Square Mile to Hectare.'),
        'ac_ha': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Acre to Hectare.'),
        'ha_ac': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Hectare to Acre.'),

        # Volume

        'l_usgal': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Litre to US Gallon.'),
        'l_ukgal': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Litre to UK Gallon.'),
        'gal_pt': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Gallon (either US or UK) to Pint.'),
        'usgal_l': QT_TRANSLATE_NOOP('Mathdocs',
                'converts US Gallon to Litre.'),
        'ukgal_l': QT_TRANSLATE_NOOP('Mathdocs',
                'converts UK Gallon to Litre.'),

        # Weight

        'oz_g': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Ounce to Gram.'),
        'lb_oz': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Pound to Ounce.'),
        'lb_g': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Pound to Gram.'),
        'lb_kg': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Pound to Kilogram.'),
        'g_oz': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Gram to Ounce.'),
        'g_lb': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Gram to Pound.'),
        'kg_oz': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Kilogram to Ounce.'),
        'kg_lb': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Kilogram to Pound.'),
        'ct_g': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Carat to Gram.'),
        'ct_oz': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Carat to Ounce.'),
        'g_ct': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Gram to Carat.'),
        'oz_ct': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Ounce to Carat.'),

        # Energy

        'wh_cl': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Watt-hour to Calorie.'),
        'wh_j': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Watt-hour to Joule.'),
        'cl_j': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Calorie to Joule.'),
        'cl_wh': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Calorie to Watt-hour.'),
        'j_cl': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Joule to Calorie.'),
        'j_wh': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Joule to Watt-hour.'),

        # Temperature

        'c_f': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Celsius to Fahrenheit.'),
        'c_k': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Celsius to Kelvin.'),
        'f_c': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Fahrenheit to Celsius.'),
        'f_k': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Fahrenheit to Kelvin.'),
        'k_c': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Kelvin to Celsius.'),
        'k_f': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Kelvin to Fahrenheit.'),

        # Power

        'kw_hp': QT_TRANSLATE_NOOP('Mathdocs',
                'converts KiloWatt to Horsepower.'),
        'hp_kw': QT_TRANSLATE_NOOP('Mathdocs',
                'converts Horsepower to KiloWatt.'),
    }
