# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModest(RPackage):
	"""Model-Based Dose-Escalation Trials

	User-friendly Shiny apps for designing and evaluating phase I cancer clinical trials, with the aim to estimate the maximum tolerated dose (MTD) of a novel drug, using a Bayesian decision procedure based on logistic regression.
	"""
	
	cran = "modest" 

	version("0.3-1", md5="1df29962e49154fb3d3778e538daa366")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
