# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustlmm(RPackage):
	"""Robust Linear Mixed Effects Models

	Implements the Robust Scoring Equations estimator to fit linear
    mixed effects models robustly.
    Robustness is achieved by modification of the scoring equations
    combined with the Design Adaptive Scale approach.
	"""
	
	homepage = "https://github.com/kollerma/robustlmm"
	cran = "robustlmm" 

	version("3.3-1", md5="14ad4e53ea8fcd008df768a2a75e0c8d")

	depends_on("r-lme4@1.1.9:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
