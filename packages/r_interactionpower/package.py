# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractionpower(RPackage):
	"""Power Analyses for Interaction Effects in Cross-Sectional
Regressions

	Power analysis for regression models which test the interaction of
    two independent variables on a single dependent variable. Includes options 
    for continuous, binary, or ordinal variables, as well as correlated 
    interacting variables. Also includes options to specify variable reliability.
    Power analyses can be done either analytically or via simulation.  Includes 
    tools for simulating single data sets and visualizing power analysis results.
    The primary functions are power_interaction_r2() and power_interaction(). 
    Please cite as: Baranger DAA, Finsaas MC, Goldstein BL, Vize CE, Lynam DR,
    Olino TM (2022). "Tutorial: Power analyses for interaction effects in 
    cross-sectional regressions." <doi:10.31234/osf.io/5ptd7>. 
	"""
	
	homepage = "https://dbaranger.github.io/InteractionPoweR/"
	cran = "InteractionPoweR" 

	version("0.2.1", md5="3d16f527579d2d8c239166deb8b89001")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-chngpt", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
