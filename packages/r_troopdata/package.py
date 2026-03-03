# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTroopdata(RPackage):
	"""Tools for Analyzing Cross-National Military Deployment and
Basing Data

	These functions generate data frames on troop deployments and military basing using U.S. Department of Defense data on overseas military deployments. This package provides functions for pulling country-year troop deployment and basing data. Subsequent versions will hopefully include cross-national data on deploying countries.
	"""
	
	homepage = "https://github.com/meflynn/troopdata"
	cran = "troopdata" 

	version("0.1.5", md5="f5711e32ba13873d20aa02f6bfea9e8a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
