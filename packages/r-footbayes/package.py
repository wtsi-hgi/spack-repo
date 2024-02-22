# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFootbayes(RPackage):
	"""Fitting Bayesian and MLE Football Models

	This is the first package allowing for the estimation,
             visualization and prediction of the most well-known 
             football models: double Poisson, bivariate Poisson,
             Skellam, student_t, diagonal-inflated bivariate Poisson, and
             zero-inflated Skellam. The package allows Hamiltonian
             Monte Carlo (HMC) estimation through the underlying Stan
             environment and Maximum Likelihood estimation (MLE, for 
             'static' models only). The model construction relies on
             the most well-known football references, such as 
             Dixon and Coles (1997) <doi:10.1111/1467-9876.00065>,
             Karlis and Ntzoufras (2003) <doi:10.1111/1467-9884.00366> and
             Egidi, Pauli and Torelli (2018) <doi:10.1177/1471082X18798414>.
	"""
	
	homepage = "https://github.com/leoegidi/footbayes"
	cran = "footBayes" 

	version("0.2.0", md5="53bdf8f0ddfd9eed868d42bad140597a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-metrology", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
