# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpat(RPackage):
	"""Change Point Analysis Tests

	Implements several statistical tests for structural change, specifically the tests featured in Horváth, Rice and Miller (in press): CUSUM (with weighted/trimmed variants), Darling-Erdös, Hidalgo-Seo, Andrews, and the new Rényi-type test.
	"""
	
	cran = "CPAT" 

	version("0.1.0", md5="3c36b6b43dd65e0f48290291668a483c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rdpack@0.9:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-purrr@0.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
