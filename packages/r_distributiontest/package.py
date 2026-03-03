# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistributiontest(RPackage):
	"""Powerful Goodness-of-Fit Tests Based on the Likelihood Ratio

	Provides new types of omnibus tests which are generally much more powerful than traditional tests (including the Kolmogorov-Smirnov, Cramer-von Mises and Anderson-Darling tests),see Zhang (2002) <doi:10.1111/1467-9868.00337>. 
	"""
	
	cran = "DistributionTest" 

	version("1.1", md5="db556c11968b838e56278f178ca55754")

	depends_on("r-mass", type=("build", "run"))
