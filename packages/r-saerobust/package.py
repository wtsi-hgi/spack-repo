# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaerobust(RPackage):
	"""Robust Small Area Estimation

	Methods to fit robust alternatives to commonly used models used in
    Small Area Estimation. The methods here used are based on best linear
    unbiased predictions and linear mixed models. At this time available models
    include area level models incorporating spatial and temporal correlation in
    the random effects.
	"""
	
	cran = "saeRobust" 

	version("0.5.0", md5="85c4e28ce48ee21624c982fe26926d7c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-aoos", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-modules", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
