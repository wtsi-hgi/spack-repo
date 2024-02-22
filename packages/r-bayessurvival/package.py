# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayessurvival(RPackage):
	"""Bayesian Survival Analysis for Right Censored Data

	Performs unadjusted Bayesian survival analysis for right censored time-to-event data. The main function, BayesSurv(), computes the posterior mean and a credible band for the survival function and for the cumulative hazard, as well as the posterior mean for the hazard, starting from a piecewise exponential (histogram) prior with Gamma distributed heights that are either independent, or have a Markovian dependence structure.
    A function, PlotBayesSurv(), is provided to easily create plots of the posterior means of the hazard, cumulative hazard and survival function, with a credible band accompanying the latter two.
    The priors and samplers are described in more detail in Castillo and Van der Pas (2020) "Multiscale Bayesian survival analysis" <arXiv:2005.02889>. In that paper it is also shown that the credible bands for the survival function and the cumulative hazard can be considered confidence bands (under mild conditions) and thus offer reliable uncertainty quantification.
	"""
	
	cran = "BayesSurvival" 

	version("0.2.0", md5="33ab6c1d69e20832c61475da83672f1a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
