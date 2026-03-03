# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMptmultiverse(RPackage):
	"""Multiverse Analysis of Multinomial Processing Tree Models

	
    Statistical or cognitive modeling usually requires a number of more or less 
    arbitrary choices creating one specific path through a 'garden of forking paths'. 
    The multiverse approach (Steegen, Tuerlinckx, Gelman, & Vanpaemel, 2016, 
    <doi:10.1177/1745691616658637>) offers a principled alternative in which results 
    for all possible combinations of reasonable modeling choices are reported. 
    MPTmultiverse performs a multiverse analysis for multinomial processing tree 
    (MPT, Riefer & Batchelder, 1988, <doi:10.1037/0033-295X.95.3.318>) models combining 
    maximum-likelihood/frequentist and Bayesian estimation approaches with 
    different levels of pooling (i.e., data aggregation). For the 
    frequentist approaches, no pooling (with and without parametric or nonparametric 
    bootstrap) and complete pooling are implemented using 
    MPTinR <https://cran.r-project.org/package=MPTinR>. 
    For the Bayesian approaches, no pooling, complete pooling, and three different 
    variants of partial pooling are implemented using 
    TreeBUGS <https://cran.r-project.org/package=TreeBUGS>. The main function is 
    fit_mpt() who performs the multiverse analysis in one call.
	"""
	
	homepage = "https://github.com/mpt-network/MPTmultiverse"
	cran = "MPTmultiverse" 

	version("0.4-2", md5="b79aec8c25b36e1ea573c82c41d5be9a")

	depends_on("r@2.11.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mptinr", type=("build", "run"))
	depends_on("r-treebugs@1.4.4:", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
