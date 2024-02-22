# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvacost(RPackage):
	"""Analyse Biological Invasion Costs with the 'InvaCost' Database

	Provides an up-to-date version of the 'InvaCost' database 
    (<doi:10.6084/m9.figshare.12668570>) in R, and
    several functions to analyse the costs of invasive alien species 
    (<doi:10.1111/2041-210X.13929>). 
	"""
	
	cran = "invacost" 

	version("1.1-6", md5="a12ce3db235d99ce718c88a454147b9e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
