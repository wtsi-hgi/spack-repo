# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdgam(RPackage):
	"""Additive Model for Ordinal Data using Laplace P-Splines

	Additive proportional odds model for ordinal data using Laplace P-splines. The combination of Laplace approximations and P-splines enable fast and flexible inference in a Bayesian framework. Specific approximations are proposed to account for the asymmetry in the marginal posterior distributions of non-penalized parameters. For more details, see Lambert and Gressani (2023) <doi:10.1177/1471082X231181173> ; Preprint: <arXiv:2210.01668>).
	"""
	
	homepage = "<https://github.com/plambertULiege/ordgam>"
	cran = "ordgam" 

	version("0.9.1", md5="0e30c3a5ff5f97bd13ec574e47ebf925")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cubicbsplines", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-marqlevalg", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
