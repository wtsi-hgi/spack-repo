# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBartcs(RPackage):
	"""Bayesian Additive Regression Trees for Confounder Selection

	Fit Bayesian Regression Additive Trees (BART) models to
    select true confounders from a large set of potential confounders and
    to estimate average treatment effect. For more information, see Kim et
    al. (2023) <doi:10.1111/biom.13833>.
	"""
	
	homepage = "https://github.com/yooyh/bartcs"
	cran = "bartcs" 

	version("1.2.1", md5="3cb2f9929d5bd8ee9ab98a135828cdbe")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-coda@0.4:", type=("build", "run"))
	depends_on("r-ggcharts", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
