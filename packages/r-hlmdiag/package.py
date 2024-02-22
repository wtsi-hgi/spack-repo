# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHlmdiag(RPackage):
	"""Diagnostic Tools for Hierarchical (Multilevel) Linear Models

	A suite of diagnostic tools for hierarchical
    (multilevel) linear models. The tools include
    not only leverage and traditional deletion diagnostics (Cook's
    distance, covratio, covtrace, and MDFFITS) but also 
    convenience functions and graphics for residual analysis. Models
    can be fit using either lmer in the 'lme4' package or lme in the 'nlme' package.
	"""
	
	homepage = "https://github.com/aloy/HLMdiag"
	cran = "HLMdiag" 

	version("0.5.0", md5="5d6ff7dd4deb7517b4b59a44ef0ecc62")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@0.9.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-diagonals", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
