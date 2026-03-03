# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScoringtools(RPackage):
	"""Credit Scoring Tools

	Grouping essential tools for credit scoring. These statistical tools may be useful for other use-cases as well but were primarily designed for it. First, there are Reject Inference methods (Ehrhardt et al. (2017) <arXiv:1903.10855>). Second, we build upon the already CRAN-available package 'discretization' to automate discretization of continuous features.
	"""
	
	homepage = "https://adimajo.github.io/scoringTools/"
	cran = "scoringTools" 

	version("0.1.3", md5="29180bed4a3092c61980bced10bff8aa")
	version("0.1.2", md5="b2a3ebd674433f166ecf1b754b947dcc")

	depends_on("r-discretization", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
