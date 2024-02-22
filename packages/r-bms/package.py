# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBms(RPackage):
	"""Bayesian Model Averaging Library

	Bayesian Model Averaging for linear models with a wide choice of (customizable) priors. Built-in priors include coefficient priors (fixed, hyper-g and empirical priors), 5 kinds of model priors, moreover model sampling by enumeration or various MCMC approaches. Post-processing functions allow for inferring posterior inclusion and model probabilities, various moments, coefficient and predictive densities. Plotting functions available for posterior model size, MCMC convergence, predictive and coefficient densities, best models representation, BMA comparison. Also includes Bayesian normal-conjugate linear model with Zellner's g prior, and assorted methods.
	"""
	
	homepage = "http://bms.zeugner.eu"
	cran = "BMS" 

	version("0.3.5", md5="81571777fbc645e28920f71f185a1919")

	depends_on("r@2.10:", type=("build", "run"))
