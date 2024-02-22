# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVwpre(RPackage):
	"""Tools for Preprocessing Visual World Data

	Gaze data from the Visual World Paradigm requires significant
    preprocessing prior to plotting and analyzing the data. This package 
    provides functions for preparing visual world eye-tracking data for 
    statistical analysis and plotting. It can prepare data for linear 
    analyses (e.g., ANOVA, Gaussian-family LMER, Gaussian-family GAMM) as
    well as logistic analyses (e.g., binomial-family LMER and binomial-family GAMM).
    Additionally, it contains various plotting functions for creating grand average and
    conditional average plots. See the vignette for samples of the functionality.
    Currently, the functions in this package are designed for handling data
    collected with SR Research Eyelink eye trackers using Sample Reports created
    in SR Research Data Viewer.  While we would like to add functionality 
    for data collected with other systems in the future, the current package is 
    considered to be feature-complete; further updates will mainly entail maintenance
	and the addition of minor functionality.
	"""
	
	cran = "VWPre" 

	version("1.2.4", md5="7143ec7e13ca42d01e46e897c2ab84f7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-rlang@0.1.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-mgcv@1.8.16:", type=("build", "run"))
	depends_on("r-shiny@0.14.2:", type=("build", "run"))
	depends_on("r-tidyr@0.6:", type=("build", "run"))
