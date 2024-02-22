# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmrr(RPackage):
	"""Generalized Linear Mixed Model (GLMM) for Binary Randomized
Response Data

	Generalized Linear Mixed Model (GLMM) for Binary Randomized Response Data.
    Includes Cauchit, Compl. Log-Log, Logistic, and Probit link functions for Bernoulli Distributed RR data.
    RR Designs: Warner, Forced Response, Unrelated Question, Kuk, Crosswise, and Triangular. 
    Reference: Fox, J-P, Veen, D. and Klotzke, K. (2018). Generalized Linear Mixed Models for Randomized Responses. Methodology. <doi:10.1027/1614-2241/a000153>.
	"""
	
	cran = "GLMMRR" 

	version("0.5.0", md5="3619092fe418ed3b2aea598394af42fd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
