# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReval(RPackage):
	"""Argument Table Generation for Sensitivity Analysis

	Simplified scenario testing and sensitivity analysis,
    redesigned to use packages 'future' and 'furrr'. Provides
    functions for generating function argument sets using
    one-factor-at-a-time (OFAT) and (sampled) permutations.
	"""
	
	homepage = "https://github.com/mkoohafkan/reval"
	cran = "reval" 

	version("3.1-0", md5="87df2ac361428fe8f1028b543aabc394")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
