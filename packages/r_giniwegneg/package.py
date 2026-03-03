# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGiniwegneg(RPackage):
	"""Computing the Gini-Based Coefficients for Weighted and Negative
Attributes

	Gini-based coefficients and plot of the ordinary and generalized curve of maximum inequality in the presence of weighted and negative attributes. 
	"""
	
	cran = "GiniWegNeg" 

	version("1.0.1", md5="34c988d038dccde655de3d991a75187c")

