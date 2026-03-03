# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalsvm(RPackage):
	"""Survival Support Vector Analysis

	Performs support vectors analysis for data sets with survival
    outcome. Three approaches are available in the package: The regression approach
    takes censoring into account when formulating the inequality constraints of
    the support vector problem. In the ranking approach, the inequality constraints
    set the objective to maximize the concordance index for comparable pairs
    of observations. The hybrid approach combines the regression and ranking
    constraints in the same model.
	"""
	
	homepage = "https://github.com/imbs-hl/survivalsvm"
	cran = "survivalsvm" 

	version("0.0.5", md5="1c9ed088736a7d2efdb52084b90b92c9")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
