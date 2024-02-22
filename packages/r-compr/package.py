# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompr(RPackage):
	"""Paired Comparison Data Analysis

	Different tools for describing and analysing paired comparison data are presented. Main methods are estimation of products scores according Bradley Terry Luce model. A segmentation of the individual could be conducted on the basis of a mixture distribution approach. The number of classes can be tested by the use of Monte Carlo simulations. This package deals also with multi-criteria paired comparison data. 
	"""
	
	cran = "CompR" 

	version("1.0", md5="f9a5e5b0fe97f5d84d47681994c830f4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
