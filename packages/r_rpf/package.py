# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpf(RPackage):
	"""Response Probability Functions

	Factor out logic
    and math common to Item Factor Analysis fitting, diagnostics, and
    analysis. It is envisioned as core support code suitable for more
    specialized IRT packages to build upon. Complete access to optimized C
    functions are made available with R_RegisterCCallable().
    This software is described in Pritikin & Falk (2020) <doi:10.1177/0146621620929431>.
	"""
	
	homepage = "https://github.com/jpritikin/rpf"
	cran = "rpf" 

	version("1.0.14", md5="53628e3b6c55a2327c37b7353ad68e31")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
