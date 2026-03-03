# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLorenzregression(RPackage):
	"""Lorenz and Penalized Lorenz Regressions

	Inference for the Lorenz and penalized Lorenz regressions. More broadly, the package proposes functions to assess inequality and graphically represent it. The Lorenz Regression procedure is introduced in Heuchenne and Jacquemain (2022) <doi:10.1016/j.csda.2021.107347>.
	"""
	
	cran = "LorenzRegression" 

	version("1.0.0", md5="f226597c9bbbdd69d13cc987fe4dec35")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-rearrangement", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
