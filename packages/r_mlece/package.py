# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlece(RPackage):
	"""Asymptotic Efficient Closed-Form Estimators for Multivariate
Distributions

	Asymptotic efficient closed-form estimators (MLEces) are provided in this package for three multivariate distributions(gamma, Weibull and Dirichlet) whose maximum likelihood estimators (MLEs) are not in closed forms. Closed-form estimators are strong consistent, and have the similar asymptotic normal distribution like MLEs. But the calculation of MLEces are much faster than the corresponding MLEs. Further details and explanations of MLEces can be found in.
    Jang, et al. (2023) <doi:10.1111/stan.12299>.
    Kim, et al. (2023) <doi:10.1080/03610926.2023.2179880>.
	"""
	
	cran = "MLEce" 

	version("2.1.0", md5="3ea827bcc33f8d29d3a6f9cbcb1d207e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-sirt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
