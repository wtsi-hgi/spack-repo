# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLwfbrook90r(RPackage):
	"""Simulate Evapotranspiration and Soil Moisture with the SVAT
Model LWF-Brook90

	Provides a flexible and easy-to use interface for the soil vegetation 
    atmosphere transport (SVAT) model LWF-BROOK90, written in Fortran.
    The model simulates daily transpiration, interception, soil and snow evaporation, 
    streamflow and soil water fluxes through a soil profile covered with vegetation, 
    as described in Hammel & Kennel (2001, ISBN:978-3-933506-16-0) and Federer et al. (2003) 
    <doi:10.1175/1525-7541(2003)004%3C1276:SOAETS%3E2.0.CO;2>. A set of high-level functions
    for model set up, execution and parallelization provides easy access to plot-level SVAT 
    simulations, as well as multi-run and large-scale applications. 
	"""
	
	homepage = "https://pschmidtwalter.github.io/LWFBrook90R/"
	cran = "LWFBrook90R" 

	version("0.5.3", md5="6b3cf893a12cc5072a07e81bc27e246e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-vegperiod@0.3:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-iterators@1.0.12:", type=("build", "run"))
	depends_on("r-dofuture@0.10:", type=("build", "run"))
	depends_on("r-future@1.19:", type=("build", "run"))
	depends_on("r-parallelly@1.30:", type=("build", "run"))
	depends_on("r-progressr@0.6:", type=("build", "run"))
