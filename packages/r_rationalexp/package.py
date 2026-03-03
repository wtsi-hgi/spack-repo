# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRationalexp(RPackage):
	"""Rationalizing Rational Expectations. Tests and Deviations

	We implement a test of the rational expectations hypothesis based on the marginal distributions of realizations and subjective beliefs from D'Haultfoeuille, Gaillac, and Maurel (2018) <doi:10.3386/w25274>. This test can be used in cases where realizations and subjective beliefs are observed in two different datasets that cannot be matched, or when they are observed in the same dataset. The package also computes the estimator of the minimal deviations from rational expectations than can be rationalized by the data. 
	"""
	
	cran = "RationalExp" 

	version("0.2.2", md5="caec8d2da5061c110c744ffe84f4ce69")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
