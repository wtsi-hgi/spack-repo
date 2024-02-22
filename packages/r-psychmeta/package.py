# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychmeta(RPackage):
	"""Psychometric Meta-Analysis Toolkit

	Tools for computing bare-bones and psychometric meta-analyses and for generating psychometric data for use in meta-analysis simulations. Supports bare-bones, individual-correction, and artifact-distribution methods for meta-analyzing correlations and d values. Includes tools for converting effect sizes, computing sporadic artifact corrections, reshaping meta-analytic databases, computing multivariate corrections for range variation, and more. Bugs can be reported to <https://github.com/psychmeta/psychmeta/issues> or <issues@psychmeta.com>.
	"""
	
	cran = "psychmeta" 

	version("2.6.5", md5="ec3767c399f0b30749a215f979d47bc2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
