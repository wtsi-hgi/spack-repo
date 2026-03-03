# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBate(RPackage):
	"""Computes Bias-Adjusted Treatment Effect

	Compute bounds for the treatment effect 
    after adjusting for the presence of omitted variables in linear  
    econometric models, according to the method of Basu (2022) <arXiv:2203.12431>. 
    You supply the data, identify the outcome and 
    treatment variables and additional regressors. The main functions
    will compute bounds for the bias-adjusted treatment effect. Many
    plot functions allow easy visualization of results.
	"""
	
	homepage = "https://github.com/dbasu-umass/bate/"
	cran = "bate" 

	version("0.1.0", md5="d97b3f83d09518b936f8b42bd3d2f6be")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-vtable", type=("build", "run"))
