# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKendall(RPackage):
	"""Kendall Rank Correlation and Mann-Kendall Trend Test

	Computes the Kendall rank correlation and Mann-Kendall
        trend test. See documentation for use of block bootstrap when
        there is autocorrelation.
	"""
	
	homepage = "http://www.stats.uwo.ca/faculty/aim"
	cran = "Kendall" 

	version("2.2.1", md5="08c745865c00e824aaf6a721a4ef742b")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
