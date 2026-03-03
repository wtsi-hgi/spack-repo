# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectiveinference(RPackage):
	"""Tools for Post-Selection Inference

	New tools for post-selection inference, for use with forward
    stepwise regression, least angle regression, the lasso, and the many means
    problem. The lasso function implements Gaussian, logistic and Cox survival
    models.
	"""
	
	cran = "selectiveInference" 

	version("1.2.5", md5="f056cbb1b72b7031b79b0a0763165bbd")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-intervals", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-adaptmcmc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
