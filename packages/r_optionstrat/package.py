# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptionstrat(RPackage):
	"""Utilizes the Black-Scholes Option Pricing Model to Perform
Strategic Option Analysis and Plot Option Strategies

	Utilizes the Black-Scholes-Merton option pricing model to 
    calculate key option analytics and perform graphical analysis of various option strategies.
    Provides functions to calculate the option premium and option
    greeks of European-style options. 
	"""
	
	cran = "optionstrat" 

	version("1.4.1", md5="9fc11d88b7928e8b307e11f520b89608")

