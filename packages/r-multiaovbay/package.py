# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiaovbay(RPackage):
	"""Classic, Nonparametric and Bayesian Two-Way Analysis of Variance
Panel

	Covers several approaches to ANOVA (Analysis of Variance), specifically studying a balanced two-factor fixed-fixed ANOVA design. It consists of four sections. The first section uses a dynamic scheme to indicate which possible alternatives to follow depending on the fulfillment of the assumptions of the model. It also presents an analysis on the fulfillment of the assumptions of linearity, homoscedasticity, normality, and independence in the residuals of the model, as well as dynamic statistical graphs on the residuals of the model. The second section presents an analysis with a non-parametric approach of Kruskal Wallis. After Kruskal Wallis, a Post-Hoc analysis of multiple comparisons on the medians of the treatments is carried out. The third section presents a classical parametric ANOVA. Following classical ANOVA, a post-hoc analysis of multiple comparisons on the medians of the treatments, factor levels by Dunn's test, and statistical graphs for the treatments and factor levels are shown. Additionally, a post-hoc analysis of multiple comparisons on the means of the treatments is done. The fourth section presents an analysis of variance under a Bayesian approach. In this section, interactive statistical graphs are presented on the posterior distributions of treatments, factor levels, and a convergence analysis of the estimated parameters, using MCMC (Markov Chain Monte Carlo). These results are displayed in an interactive glossy panel which allows modification of the test arguments, contains interactive statistical plots, and presents automatic conclusions depending on the fulfillment of the assumptions of the balanced two-factor fixed ANOVA model.
	"""
	
	cran = "Multiaovbay" 

	version("0.1.0", md5="faaef0dac56fa83e6ab782b30eda0819")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))
	depends_on("r-ggstatsplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-pmcmrplus", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
