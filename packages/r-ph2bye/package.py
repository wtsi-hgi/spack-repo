# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPh2bye(RPackage):
	"""Phase II Clinical Trial Design Using Bayesian Methods

	Calculate the Bayesian posterior/predictive probability and
    determine the sample size and stopping boundaries for single-arm Phase II design.
	"""
	
	homepage = "https://allen.shinyapps.io/BayesDesign/"
	cran = "ph2bye" 

	version("0.1.4", md5="c7239b7b35e05d9f068a2fa844576aa1")

	depends_on("r-animation", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
