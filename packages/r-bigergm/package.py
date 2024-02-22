# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigergm(RPackage):
	"""Fit, Simulate, and Diagnose Hierarchical Exponential-Family
Models for Big Networks

	A toolbox to analyze and simulate large networks based on hierarchical exponential-family random graph models (HERGMs).'bigergm' implements the estimation for large networks efficiently on large networks building on the 'lighthergm' package. Moreover, the package contains tools for simulating networks with local dependence to assess the estimates' goodness-of-fit.
	"""
	
	cran = "bigergm" 

	version("1.1.0", md5="e8bfdaf6498af1777b3ea3653bf8804e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ergm@4.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10.5:", type=("build", "run"))
	depends_on("r-network@1.16:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
