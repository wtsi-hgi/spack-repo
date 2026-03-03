# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFixest(RPackage):
	"""Fast Fixed-Effects Estimations

	Fast and user-friendly estimation of econometric models with multiple fixed-effects. Includes ordinary least squares (OLS), generalized linear models (GLM) and the negative binomial.
    The core of the package is based on optimized parallel C++ code, scaling especially well for large data sets. The method to obtain the fixed-effects coefficients is based on Berge (2018) <https://github.com/lrberge/fixest/blob/master/_DOCS/FENmlm_paper.pdf>.
    Further provides tools to export and view the results of several estimations with intuitive design to cluster the standard-errors.
	"""
	
	homepage = "https://lrberge.github.io/fixest/"
	cran = "fixest" 

	version("0.11.2", md5="9d2027d25c8a0081b878554544caf58b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dreamerr@1.2.3:", type=("build", "run"))
