# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnreadr(RPackage):
	"""MNREAD Parameters Estimation and Curve Plotting

	Allows to analyze the reading data obtained with the MNREAD Acuity 
    Chart, a continuous-text reading acuity chart for normal and low vision. 
    Provides the necessary functions to plot the MNREAD curve and estimate 
    automatically the four MNREAD parameters: Maximum Reading Speed, 
    Critical Print Size, Reading Acuity and Reading Accessibility Index.
    Parameters can be estimated either with the standard method 
    or with a nonlinear mixed-effects (NLME) modeling. 
    See Calabrese et al. 2018 for more details <doi:10.1167/18.1.8>.
	"""
	
	homepage = "https://legge.psych.umn.edu/mnread-acuity-charts"
	cran = "mnreadR" 

	version("2.1.7", md5="9e981dbf2dd2ba271e243f518d76a0aa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
