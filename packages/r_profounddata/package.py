# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfounddata(RPackage):
	"""Downloading and Exploring Data from the PROFOUND Database

	Provides an R interface for the PROFOUND database <doi:10.5880/PIK.2019.008>. The 
    PROFOUND database contains a wide range of data  to evaluate vegetation models and simulate climate 
    impacts at the forest stand scale. It includes 9 forest sites across Europe, and provides for them a site 
    description as well as soil, climate, CO2, Nitrogen deposition, tree-level, forest stand-level 
    and remote sensing data. Moreover, for a subset of 5 sites, also time series of carbon fluxes, 
    energy balances and soil water are available. 
	"""
	
	homepage = "https://cost-fp1304-profound.github.io/ProfoundData/"
	cran = "ProfoundData" 

	version("0.2.1", md5="dbf7f0cd8ecb3dbbbc2527b1b7e4721f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sqldf@0.4.10:", type=("build", "run"))
	depends_on("r-dbi@0.5.1:", type=("build", "run"))
	depends_on("r-rsqlite@1.1.2:", type=("build", "run"))
	depends_on("r-rnetcdf@1.9.1:", type=("build", "run"))
	depends_on("r-settings@0.2.4:", type=("build", "run"))
	depends_on("r-zoo@1.7.14:", type=("build", "run"))
