# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAddhaz(RPackage):
	"""Binomial and Multinomial Additive Hazard Models

	Functions to fit the binomial and multinomial additive hazard models and to estimate the contribution of diseases/conditions to the disability prevalence, as proposed by Nusselder and Looman (2004) and extended by Yokota et al (2017).
	"""
	
	cran = "addhaz" 

	version("0.5", md5="845dfc8477f8dd22b8967e884b7c5601")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-boot@1.3.17:", type=("build", "run"))
	depends_on("r-matrix@1.2.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
