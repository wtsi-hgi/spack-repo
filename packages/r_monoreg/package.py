# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonoreg(RPackage):
	"""Bayesian Monotonic Regression Using a Marked Point Process
Construction

	An extended version of the nonparametric Bayesian monotonic regression procedure described in Saarela & Arjas (2011) <DOI:10.1111/j.1467-9469.2010.00716.x>, allowing for multiple additive monotonic components in the linear predictor, and time-to-event outcomes through case-base sampling. The extension and its applications, including estimation of absolute risks, are described in Saarela & Arjas (2015) <DOI:10.1111/sjos.12125>. The package also implements the nonparametric ordinal regression model described in Saarela, Rohrbeck & Arjas <DOI:10.1214/22-BA1310>.
	"""
	
	cran = "monoreg" 

	version("2.1", md5="3d0009abe46fedc0686c6f117c7fda2f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
