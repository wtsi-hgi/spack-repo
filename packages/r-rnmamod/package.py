# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnmamod(RPackage):
	"""Bayesian Network Meta-Analysis with Missing Participants

	A comprehensive suite of functions to perform and visualise 
    pairwise and network meta-analysis with aggregate binary or continuous
    missing participant outcome data. The package covers core Bayesian one-stage
    models implemented in a systematic review with multiple interventions, 
    including fixed-effect and random-effects network meta-analysis, 
    meta-regression, evaluation of the consistency assumption via the 
    node-splitting approach and the unrelated mean effects model, and 
    sensitivity analysis. Missing participant outcome data are addressed in all 
    models of the package. The package also offers a rich, user-friendly 
    visualisation toolkit that aids in appraising and interpreting the results 
    thoroughly and preparing the manuscript for journal submission. 
    The visualisation tools comprise the network plot, forest plots, panel of 
    diagnostic plots, heatmaps on the extent of missing participant outcome data
    in the network, league heatmaps on estimation and prediction, rankograms, 
    Bland-Altman plot, leverage plot, deviance scatterplot, heatmap of 
    robustness, and barplot of Kullback-Leibler divergence. The package also 
    allows the user to export the results to an Excel file at the working 
    directory.
	"""
	
	homepage = "https://CRAN.R-project.org/package=rnmamod"
	cran = "rnmamod" 

	version("0.3.0", md5="6ee66555783fe2aead8f6826300bcb12")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-gemtc", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mcmcplots", type=("build", "run"))
	depends_on("r-netmeta", type=("build", "run"))
	depends_on("r-pcnetmeta", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
