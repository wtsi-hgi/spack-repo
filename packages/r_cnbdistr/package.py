# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnbdistr(RPackage):
	"""Conditional Negative Binomial Distribution

	Provided R functions for working with the Conditional Negative Binomial distribution.
	"""
	
	cran = "cnbdistr" 

	version("1.0.1", md5="8b42e2783aae0b0192efea40cfd52328")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-hypergeo@1.2.13:", type=("build", "run"))
