# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfdmcv(RPackage):
	"""General Hypothesis Testing Problems for Multivariate
Coefficients of Variation

	Performs test procedures for general hypothesis testing problems for four multivariate coefficients of variation (Ditzhaus and Smaga, 2023 <arXiv:2301.12009>). We can verify the global hypothesis about equality as well as the particular hypotheses defined by contrasts, e.g., we can conduct post hoc tests. We also provide the simultaneous confidence intervals for contrasts.
	"""
	
	cran = "GFDmcv" 

	version("0.1.0", md5="ef98d9095427640665e8b425c7227ea2")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hsaur", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
