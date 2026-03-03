# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtscr(RPackage):
	"""Multidimensional Top Scoring for Creativity Research

	Implementation of Multidimensional Top Scoring
    method for creativity assessment proposed in
    Boris Forthmann, Maciej Karwowski, Roger E. Beaty (2023) <doi:10.1037/aca0000571>.
	"""
	
	cran = "mtscr" 

	version("1.0.1", md5="69a789cd394e0381ff55046391c66db7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
