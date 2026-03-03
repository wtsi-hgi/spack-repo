# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrsTest(RPackage):
	"""GRS Test for Portfolio Efficiency, Its Statistical Power
Analysis, and Optimal Significance Level Calculation

	Computational resources for test proposed by Gibbons, Ross, Shanken (1989)<DOI:10.2307/1913625>.
	It also has the functions for the power analysis and the choice of the optimal level of significance.
	The optimal level is determined by minimizing the expected loss from hypothesis testing. 
	"""
	
	cran = "GRS.test" 

	version("1.2", md5="b94708c58869783ff8fddba7153bfdaf")

