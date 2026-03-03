# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExact2x2(RPackage):
	"""Exact Tests and Confidence Intervals for 2x2 Tables

	Calculates conditional exact tests (Fisher's exact test, Blaker's exact test, or  exact McNemar's test) and unconditional exact tests (including score-based tests on differences in proportions, ratios of proportions, and odds ratios, and Boshcloo's test) with appropriate matching confidence intervals, and provides power and sample size calculations. Gives melded confidence intervals for the binomial case (Fay, et al, 2015, <DOI:10.1111/biom.12231>). Gives boundary-optimized rejection region test (Gabriel, et al, 2018, <DOI:10.1002/sim.7579>), an unconditional exact test for the situation where the controls are all expected to fail. Gives confidence intervals compatible with exact McNemar's or sign tests (Fay and Lumbard, 2021, <DOI:10.1002/sim.8829>). For review of these kinds of exact tests see Fay and Hunsberger (2021, <DOI:10.1214/21-SS131>).
	"""
	
	cran = "exact2x2" 

	version("1.6.9", md5="8eb9778300f5710afacf556861b07ebc", url="https://cran.r-project.org/src/contrib/exact2x2_1.6.9.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-exactci", type=("build", "run"))
	depends_on("r-ssanv", type=("build", "run"))
