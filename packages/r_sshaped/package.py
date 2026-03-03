# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSshaped(RPackage):
	"""Nonparametric, Tuning-Free Estimation of S-Shaped Functions

	Estimation of an S-shaped function and its corresponding inflection point via a least squares approach. A sequential mixed primal-dual based algorithm is implemented for the fast computation. Details can be found in Feng et al. (2022) <doi:10.1111/rssb.12481>.
	"""
	
	cran = "Sshaped" 

	version("1.1", md5="48f53a8bc5ca82cd65a2b4aa20a3b000")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
