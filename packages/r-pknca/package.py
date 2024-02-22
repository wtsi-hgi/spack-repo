# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPknca(RPackage):
	"""Perform Pharmacokinetic Non-Compartmental Analysis

	Compute standard Non-Compartmental Analysis (NCA) parameters for
    typical pharmacokinetic analyses and summarize them.
	"""
	
	homepage = "https://billdenney.github.io/pknca/"
	cran = "PKNCA" 

	version("0.10.2", md5="fe73e3d2402a67f4043be9d3f703f55a")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
