# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianreasoning(RPackage):
	"""Plot Positive and Negative Predictive Values for Medical Tests

	Functions to plot and help understand positive and negative
    predictive values (PPV and NPV), and their relationship with
    sensitivity, specificity, and prevalence. See Akobeng, A.K. (2007)
    <doi:10.1111/j.1651-2227.2006.00180.x> for a theoretical overview of
    the technical concepts and Navarrete et al. (2015) for a practical
    explanation about the importance of their understanding
    <doi:10.3389/fpsyg.2015.01327>.
	"""
	
	homepage = "https://github.com/gorkang/BayesianReasoning"
	cran = "BayesianReasoning" 

	version("0.4.2", md5="c55c1172def7bd385467c5fee338278e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggforce@0.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
