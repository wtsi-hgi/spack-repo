# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquivalencetest(RPackage):
	"""Equivalence Test for the Means of Two Normal Distributions

	Two methods for performing equivalence test for the means of two (test and reference) normal distributions are implemented. The null hypothesis of the equivalence test is that the absolute difference between the two means are greater than or equal to the equivalence margin and the alternative is that the absolute difference is less than the margin. Given that the margin is often difficult to obtain a priori, it is assumed to be a constant multiple of the standard deviation of the reference distribution. The first method assumes a fixed margin which is a constant multiple of the estimated standard deviation of the reference data and whose variability is ignored. The second method takes into account the margin variability. In addition, some tools to summarize and illustrate the data and test results are included to facilitate the evaluation of the data and interpretation of the results.
	"""
	
	cran = "equivalenceTest" 

	version("0.0.1.1", md5="8d64e6df53a5c432880ab7c4b7c0949a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
