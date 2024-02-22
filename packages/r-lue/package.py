# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLue(RPackage):
	"""Light Use Efficiency Model to Estimate Biomass and YIELD with
and Without Vapour Pressure Deficit

	Contains LUE_BIOMASS(),LUE_BIOMASS_VPD(), LUE_YIELD() and LUE_YIELD_VPD() to estimate aboveground biomass and crop yield firstly by calculating the Absorbed Photosynthetically Active Radiation (APAR) and secondly the actual values of light use efficiency with and without vapour presure deficit Shi et al.(2007) <doi:10.2134/agronj2006.0260>.
	"""
	
	cran = "lue" 

	version("0.2.1", md5="e6db4db30f048487dfabbeec2595ad4a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
