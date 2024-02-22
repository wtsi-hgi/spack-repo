# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFido(RPackage):
	"""Bayesian Multinomial Logistic Normal Regression

	Provides methods for fitting and inspection of Bayesian Multinomial Logistic Normal Models using MAP estimation 
 and Laplace Approximation as developed in Silverman et. Al. (2022) <https://www.jmlr.org/papers/v23/19-882.html>. Key functionality is implemented in C++ for 
 scalability. 'fido' replaces the previous package 'stray'.
	"""
	
	homepage = "https://jsilve24.github.io/fido/"
	cran = "fido" 

	version("1.0.4", md5="f10bd88cd7e191e7d4ad0c3f74b84843")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidybayes", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-rcppziggurat", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
