# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRubias(RPackage):
	"""Bayesian Inference from the Conditional Genetic Stock
Identification Model

	Implements Bayesian inference for the conditional genetic 
    stock identification model.  It allows inference of mixed fisheries and also 
    simulation of mixtures to predict accuracy.  A full description of the underlying
    methods is available in a recently published article in the
    Canadian Journal of Fisheries and Aquatic Sciences: <doi:10.1139/cjfas-2018-0016>.
	"""
	
	cran = "rubias" 

	version("0.3.4", md5="d250c33b9e1b04539114aa54c4c0b9c0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
