# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscreteinverseweibull(RPackage):
	"""Discrete Inverse Weibull Distribution

	Probability mass function, distribution function, quantile function, random generation and parameter estimation for the discrete inverse Weibull distribution.
	"""
	
	cran = "DiscreteInverseWeibull" 

	version("1.0.2", md5="3f9b38b9926e50715952dda647f5cc94")

	depends_on("r-rsolnp", type=("build", "run"))
