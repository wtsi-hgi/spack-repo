# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlipr(RPackage):
	"""Flexible Inference via Permutations in R

	A flexible permutation framework for making 
    inference such as point estimation, confidence 
    intervals or hypothesis testing, on any kind of data, 
    be it univariate, multivariate, or more complex such 
    as network-valued data, topological data, functional 
    data or density-valued data.
	"""
	
	homepage = "https://LMJL-Alea.github.io/flipr/"
	cran = "flipr" 

	version("0.3.3", md5="6cf2880eae3f0c041f774eca5b84e82c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
