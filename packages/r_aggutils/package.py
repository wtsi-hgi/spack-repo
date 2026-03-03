# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAggutils(RPackage):
	"""Utilities for Aggregating Probabilistic Forecasts

	Provides several methods for aggregating probabilistic forecasts. You have a group of
    people who have made probabilistic forecasts for the same event. You want to take advantage of
    the "wisdom of the crowd" and combine these forecasts in some sensible way. This package
    provides implementations of several strategies, including geometric mean of odds, an extremized
    aggregate (Neyman, Roughgarden (2021) <doi:10.1145/3490486.3538243>), and "high-density trimmed
    mean" (Powell et al. (2022) <doi:10.1037/dec0000191>).
	"""
	
	homepage = "https://github.com/forecastingresearch/aggutils"
	cran = "aggutils" 

	version("1.0.2", md5="c9cb2cbb00ab98ccc644406bc2c43c6d")

	depends_on("r-docstring", type=("build", "run"))
