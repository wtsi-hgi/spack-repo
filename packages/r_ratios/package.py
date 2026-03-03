# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatios(RPackage):
	"""Calculating Ratios Between Two Data Sets and Correction for
Adhering Particles on Plants

	Calculation of ratios between two data sets containing environmental data like
    element concentrations by different methods. Additionally plant element 
    concentrations can be corrected for adhering particles (soil, airborne dust).
	"""
	
	cran = "ratios" 

	version("1.2.0", md5="b611316b58b22cb817857532adc3e2d3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
