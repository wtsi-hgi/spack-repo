# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscretelaplace(RPackage):
	"""Discrete Laplace Distributions

	Probability mass function, distribution function, quantile function, random generation and estimation for the skew discrete Laplace distributions.
	"""
	
	cran = "DiscreteLaplace" 

	version("1.1.1", md5="ffa739ca8eb204ddcdf865f302978ac6")

