# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultnonparam(RPackage):
	"""Multivariate Nonparametric Methods

	A collection of multivariate nonparametric methods, selected in part to support an MS level course in nonparametric statistical methods. Methods include adjustments for multiple comparisons, implementation of multivariate Mann-Whitney-Wilcoxon testing, inversion of these tests to produce a confidence region, some permutation tests for linear models, and some algorithms for calculating exact probabilities associated with one- and two- stage testing involving Mann-Whitney-Wilcoxon statistics.  Supported by grant NSF DMS 1712839.  See Kolassa and Seifu (2013) <doi:10.1016/j.acra.2013.03.006>.
	"""
	
	cran = "MultNonParam" 

	version("1.3.9", md5="6e6fa4ab4d7fe253ffd807feb13eda08")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-icsnp", type=("build", "run"))
