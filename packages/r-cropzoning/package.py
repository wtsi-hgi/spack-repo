# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCropzoning(RPackage):
	"""Climate Crop Zoning Based in Air Temperature for Brazil

	Climate crop zoning based in minimum and maximum air temperature. The data used in the package are from 'TerraClimate' dataset (<https://www.climatologylab.org/terraclimate.html>), but, it have been calibrated with automatic weather stations  of National Meteorological Institute of Brazil.  The climate crop zoning of this package can be run for all the Brazilian territory.
	"""
	
	cran = "cropZoning" 

	version("1.0.3", md5="af2f81830ae9c8eef87671ecc832c486")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
