# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbscci(RPackage):
	"""Blyth-Still-Casella Confidence Interval

	Provides a fast calculation of the Blyth-Still-Casella confidence interval. The implementation follows the 'StatXact' 9 manual (Cytel 2010) and "Refining Binomial Confidence Intervals" by George Casella (1986) <doi:10.2307/3314658>.
	"""
	
	cran = "rbscCI" 

	version("0.1.1", md5="fa4b4888f8b2dfc0edad8cf5bd9498c9")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
