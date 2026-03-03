# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNuts(RPackage):
	"""Convert European Regional Data

	Motivated by changing administrative boundaries over time,
    the 'nuts' package can convert European regional data with NUTS codes
    between versions (2006, 2010, 2013, 2016 and 2021) and levels (NUTS 1,
    NUTS 2 and NUTS 3). The package uses spatial interpolation as in Lam
    (1983) <doi:10.1559/152304083783914958> based on granular (100m x
    100m) area, population and land use data provided by the European
    Commission's Joint Research Center.
	"""
	
	homepage = "https://docs.ropensci.org/nuts/"
	cran = "nuts" 

	version("1.0.0", md5="65f663fdee4d8bd16a1c1b1d26ed9f4d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
