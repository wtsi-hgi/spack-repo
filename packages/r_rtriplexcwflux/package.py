# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtriplexcwflux(RPackage):
	"""Carbon-Water Coupled Model

	A carbon-water coupled model (TRIPLEX-CW-Flux) is based on two well-established models, TRIPLEX-Flux model and Penman–Monteith model, integrates soil water and water vapor pressure deficits into the stomata conductance submodule to estimate net ecosystem production and evapotranspiration in forest ecosystems.<https://github.com/ShulanSun/rTRIPLEX_CW_Flux>.
	"""
	
	homepage = "https://github.com/ShulanSun/rTRIPLEX_CW_Flux"
	cran = "rTRIPLEXCWFlux" 

	version("0.2.0", md5="997286f85b032e79dd8454bea31c5689")

	depends_on("r@2.10:", type=("build", "run"))
