# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsa(RPackage):
	"""Response Surface Analysis

	Advanced response surface analysis. The main function RSA computes
    and compares several nested polynomial regression models (full second- or 
    third-order polynomial, shifted and rotated squared difference model, 
    rising ridge surfaces, basic squared difference model, asymmetric or 
    level-dependent congruence effect models). The package provides plotting 
    functions for 3d wireframe surfaces, interactive 3d plots, and contour plots. 
    Calculates many surface parameters (a1 to a5, principal axes, stationary point,
    eigenvalues) and provides standard, robust, or bootstrapped standard errors
    and confidence intervals for them.
	"""
	
	cran = "RSA" 

	version("0.10.6", md5="1b2c85e04306a3bd2c40b6cad464fa70")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-lavaan@0.5.20:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-aplpack", type=("build", "run"))
