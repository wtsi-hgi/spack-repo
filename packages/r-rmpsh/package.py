# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmpsh(RPackage):
	"""Recursive Modified Pattern Search on Hyper-Rectangle

	Optimization of any Black-Box/Non-Convex Function on Hyper-Rectangular Parameter Space. It uses a Variation of Pattern Search Technique. Described in the paper : Das (2016) <arXiv:1604.08616> .
	"""
	
	cran = "RMPSH" 

	version("1.1.1", md5="3ea3016621f09155182d47b6b28293ec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
