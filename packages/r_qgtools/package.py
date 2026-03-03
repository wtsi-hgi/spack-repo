# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgtools(RPackage):
	"""Generalized Quantitative Genetics Data Analyses

	Two linear mixed model approaches: REML(restricted maximum likelihood) and MINQUE (minimum norm quadratic unbiased estimation) approaches and several resampling techniques are integrated for various quantitative genetics analyses. With these two types of approaches, various unbalanced data structures, missing data, and any irregular genetic  mating designs can be analyzed and statistically tested. This package also offers fast computations for many large data sets. 
	"""
	
	cran = "qgtools" 

	version("2.0", md5="6d6626797729ece9e88c7cb4acefcf0c")

