# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstat(RPackage):
	"""Spatial Point Pattern Analysis, Model-Fitting, Simulation, Tests.

	Comprehensive open-source toolbox for analysing Spatial Point Patterns.
	Focused mainly on two-dimensional point patterns, including
	multitype/marked points, in any spatial region. Also supports
	three-dimensional point patterns, space-time point patterns in any number
	of dimensions, point patterns on a linear network, and patterns of other
	geometrical objects. Supports spatial covariate data such as pixel images.
	Contains over 2000 functions for plotting spatial data, exploratory data
	analysis, model-fitting, simulation, spatial sampling, model diagnostics,
	and formal inference. Data types include point patterns, line segment
	patterns, spatial windows, pixel images, tessellations, and linear
	networks. Exploratory methods include quadrat counts, K-functions and their
	simulation envelopes, nearest neighbour distance and empty space
	statistics, Fry plots, pair correlation function, kernel smoothed
	intensity, relative risk estimation with cross-validated bandwidth
	selection, mark correlation functions, segregation indices, mark dependence
	diagnostics, and kernel estimates of covariate effects. Formal hypothesis
	tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte Carlo,
	Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo) and tests
	for covariate effects (Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov, ANOVA)
	are also supported. Parametric models can be fitted to point pattern data
	using the functions ppm(), kppm(), slrm(), dppm() similar to glm(). Types
	of models include Poisson, Gibbs and Cox point processes, Neyman-Scott
	cluster processes, and determinantal point processes. Models may involve
	dependence on covariates, inter-point interaction, cluster formation and
	dependence on marks. Models are fitted by maximum likelihood, logistic
	regression, minimum contrast, and composite likelihood methods. A model can
	be fitted to a list of point patterns (replicated point pattern data) using
	the function mppm(). The model can include random effects and fixed effects
	depending on the experimental design, in addition to all the features
	listed above. Fitted point process models can be simulated, automatically.
	Formal hypothesis tests of a fitted model are supported (likelihood ratio
	test, analysis of deviance, Monte Carlo tests) along with basic tools for
	model selection (stepwise(), AIC()) and variable selection (sdr). Tools for
	validating the fitted model include simulation envelopes, residuals,
	residual plots and Q-Q plots, leverage and influence diagnostics, partial
	residuals, and added variable plots."""

	cran = "spatstat"

	license("GPL-2.0-or-later")

	version("3.0-7", md5="968cd3cfe05fba659ccf5c3142d23443")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-data@3.0.1:", type=("build", "run"))
	depends_on("r-spatstat-geom@3.2.7:", type=("build", "run"))
	depends_on("r-spatstat-random@3.2.1:", type=("build", "run"))
	depends_on("r-spatstat-explore@3.2.5:", type=("build", "run"))
	depends_on("r-spatstat-model@3.2.8:", type=("build", "run"))
	depends_on("r-spatstat-linnet@3.1.3:", type=("build", "run"))
	depends_on("r-spatstat-utils@3.0.3:", type=("build", "run"))
