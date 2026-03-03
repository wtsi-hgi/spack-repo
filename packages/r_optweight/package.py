# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptweight(RPackage):
	"""Targeted Stable Balancing Weights Using Optimization

	Use optimization to estimate weights that balance covariates for binary, multinomial, and continuous treatments in the spirit of Zubizarreta (2015) <doi:10.1080/01621459.2015.1023805>. The degree of balance can be specified for each covariate. In addition, sampling weights can be estimated that allow a sample to generalize to a population specified with given target moments of covariates.
	"""
	
	cran = "optweight" 

	version("0.2.5", md5="8492401553d118680b5d1c62dc1bc426")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-osqp@0.6.0.2:", type=("build", "run"))
	depends_on("r-matrix@1.2.13:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
