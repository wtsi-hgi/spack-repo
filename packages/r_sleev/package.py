# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSleev(RPackage):
	"""Semiparametric Likelihood Estimation with Errors in Variables

	Efficient regression analysis under general two-phase sampling, where Phase I includes error-prone data and Phase II contains validated data on a subset.
	"""
	
	cran = "sleev" 

	version("1.0.3", md5="dedd7d4c63e0acb57716f8cfdb69edbb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
