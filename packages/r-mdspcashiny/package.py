# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdspcashiny(RPackage):
	"""Interactive Document for Working with Multidimensional Scaling
and Principal Component Analysis

	An interactive document on  the topic of multidimensional scaling and principal component analysis using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://kartikeyabolar.shinyapps.io/MDS_PCAShiny/>.
	"""
	
	cran = "MDSPCAShiny" 

	version("0.1.0", md5="f59e3944d90307e7df301b9205a1a094")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
