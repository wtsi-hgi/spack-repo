# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinib(RPackage):
	"""Sum of Independent Non-Identical Binomial Random Variables

	Density, distribution function, quantile function 
	and random generation for the sum of independent non-identical
	binomial distribution with parameters code{size} and code{prob}.
	"""
	
	cran = "sinib" 

	version("1.0.0", md5="477829f7c9b054f584bed94c3dbe451e")

