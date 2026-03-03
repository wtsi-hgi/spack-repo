# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmp(RPackage):
	"""Statistical Test for the Multivariate Point Null Hypotheses

	A testing framework for testing the multivariate point null hypothesis. 
    A testing framework described in Elder et al. (2022) <arXiv:2203.01897> to test the multivariate point null hypothesis.  After the user selects a parameter of interest and defines the assumed data generating mechanism, this information should be encoded in functions for the parameter estimator and its corresponding influence curve. Some parameter and data generating mechanism combinations have codings in this package, and are explained in detail in the article.
	"""
	
	cran = "amp" 

	version("1.0.0", md5="8a2d89c1fdc9b2fd9820e9043ce1573e")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
