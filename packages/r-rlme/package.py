# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlme(RPackage):
	"""Rank-Based Estimation and Prediction in Random Effects Nested
Models

	Estimates robust rank-based fixed effects and predicts robust
    random effects in two- and three- level random effects nested models.
    The methodology is described in Bilgic & Susmann (2013) <https://journal.r-project.org/archive/2013/RJ-2013-027/>.
	"""
	
	cran = "rlme" 

	version("0.5", md5="0806f462364fd577621646c5b2fafe34")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
