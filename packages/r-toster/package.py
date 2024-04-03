# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToster(RPackage):
	"""Two One-Sided Tests (TOST) Equivalence Testing

	Two one-sided tests (TOST) procedure to test equivalence for t-tests, correlations, differences between proportions, and meta-analyses, including power analysis for t-tests and correlations. Allows you to specify equivalence bounds in raw scale units or in terms of effect sizes. See: Lakens (2017) <doi:10.1177/1948550617697177>.
	"""
	
	homepage = "https://aaroncaldwell.us/TOSTERpkg/"
	cran = "TOSTER" 

	version("0.8.1", md5="68d6aa9131d0817db79fe2f28a9e406c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jmvcore@0.9.6.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
	depends_on("r-distributional", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
