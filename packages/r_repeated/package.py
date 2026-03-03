# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepeated(RPackage):
	"""Non-Normal Repeated Measurements Models

	Various functions to fit models for non-normal repeated
    measurements, such as Binary Random Effects Models with Two Levels of Nesting,
    Bivariate Beta-binomial Regression Models, Marginal Bivariate Binomial Regression Models,
    Cormack capture-recapture models, Continuous-time Hidden Markov Chain Models, 
    Discrete-time Hidden Markov Chain Models,
    Changepoint Location Models using a Continuous-time Two-state Hidden Markov Chain,
    generalized nonlinear autoregression models, multivariate Gaussian copula models,
    generalized non-linear mixed models with one random effect,  
    generalized non-linear mixed models using h-likelihood for one random effect, 
    Repeated Measurements Models for Counts with Frailty or Serial Dependence,
    Repeated Measurements Models for Continuous Variables with Frailty or Serial Dependence,
    Ordinal Random Effects Models with Dropouts, marginal homogeneity models for square
    contingency tables, correlated negative binomial models with Kalman update.
    References include Lindsey's text books, 
    JK Lindsey (2001) <isbn:10-0198508123> and JK Lindsey (1999) <isbn:10-0198505590>.
	"""
	
	homepage = "https://www.commanster.eu/rcode.html"
	cran = "repeated" 

	version("1.1.7", md5="30f9c3df879619f6878d850039c91544")

	depends_on("r@1.4:", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
