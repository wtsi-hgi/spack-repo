# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmartsva(RPackage):
	"""Fast and Robust Surrogate Variable Analysis

	Introduces a fast and efficient Surrogate Variable Analysis algorithm that captures variation of unknown sources (batch effects) for high-dimensional data sets. The algorithm is built on the 'irwsva.build' function of the 'sva' package and proposes a revision on it that achieves an order of magnitude faster running time while trading no accuracy loss in return.
	"""
	
	cran = "SmartSVA" 

	version("0.1.3", md5="e410f7887af9f257d5e419374b52bfeb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-isva", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
