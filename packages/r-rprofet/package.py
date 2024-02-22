# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprofet(RPackage):
	"""WOE Transformation and Scorecard Builder

	Performs all steps in the credit scoring process. This package allows the user to follow all the necessary steps for building an effective scorecard. It provides the user functions for coarse binning of variables, Weights of Evidence (WOE) transformation, variable clustering, custom binning, visualization, and scaling of logistic regression coefficients. The results will generate a scorecard that can be used as an effective credit scoring tool to evaluate risk. For complete details on the credit scoring process, see Siddiqi (2005, ISBN:047175451X).  
	"""
	
	cran = "Rprofet" 

	version("2.2.1", md5="1009d833038e577f7349fa1319f63ce7")

	depends_on("r-binr", type=("build", "run"))
	depends_on("r-clustofvar", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
