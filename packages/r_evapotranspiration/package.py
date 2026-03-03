# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvapotranspiration(RPackage):
	"""Modelling Actual, Potential and Reference Crop
Evapotranspiration

	Uses data and constants to calculate potential evapotranspiration (PET) and actual evapotranspiration (AET) from 21 different formulations including Penman, Penman-Monteith FAO 56, Priestley-Taylor and Morton formulations.
	"""
	
	cran = "Evapotranspiration" 

	version("1.16", md5="ee36addd3c27e4d3607e3e02a89e4383")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
