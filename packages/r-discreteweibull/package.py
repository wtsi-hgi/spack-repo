# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscreteweibull(RPackage):
	"""Discrete Weibull Distributions (Type 1 and 3)

	Probability mass function, distribution function, quantile function, random generation and parameter estimation for the type I and III discrete Weibull distributions.
	"""
	
	cran = "DiscreteWeibull" 

	version("1.1", md5="d8cffa942fd44b3ca765366634d95336")

	depends_on("r-rsolnp", type=("build", "run"))
