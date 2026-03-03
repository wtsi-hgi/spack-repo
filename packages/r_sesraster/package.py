# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSesraster(RPackage):
	"""Raster Randomization for Null Hypothesis Testing

	Randomization of presence/absence species distribution raster
    data with or without including spatial structure for calculating
    standardized effect sizes and testing null hypothesis. The
    randomization algorithms are based on classical algorithms for
    matrices (Gotelli 2000, <doi:10.2307/177478>) implemented for raster
    data.
	"""
	
	homepage = "https://CRAN.R-project.org/package=SESraster"
	cran = "SESraster" 

	version("0.7.0", md5="bbc889fe23f65e0bb041e834b71966c6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
