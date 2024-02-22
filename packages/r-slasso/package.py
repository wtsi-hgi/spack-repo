# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlasso(RPackage):
	"""S-LASSO Estimator for the Function-on-Function Linear Regression

	Implements the smooth LASSO estimator for the function-on-function linear regression model described in Centofanti et al. (2020) <arXiv:2007.00529>.
	"""
	
	homepage = "https://github.com/unina-sfere/slasso"
	cran = "slasso" 

	version("1.0.0", md5="1f06d53a362ba0db7a06113196afacb7")

	depends_on("r-inline", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-cxxfunplus", type=("build", "run"))
