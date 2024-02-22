# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcar(RPackage):
	"""Formal Concept Analysis

	Provides tools to perform fuzzy formal concept
    analysis, presented in Wille (1982) <doi:10.1007/978-3-642-01815-2_23>
    and in Ganter and Obiedkov (2016) <doi:10.1007/978-3-662-49291-8>.  It
    provides functions to load and save a formal context, extract its
    concept lattice and implications.  In addition, one can use the
    implications to compute semantic closures of fuzzy sets and, thus,
    build recommendation systems.
	"""
	
	homepage = "https://github.com/Malaga-FCA-group/fcaR"
	cran = "fcaR" 

	version("1.2.2", md5="428fe597a07d2aa52615cf07761e0f82")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-fractional", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-posetr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-registry", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tikzdevice", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
