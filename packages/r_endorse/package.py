# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REndorse(RPackage):
	"""Bayesian Measurement Models for Analyzing Endorsement
Experiments

	Fit the hierarchical and non-hierarchical Bayesian measurement models proposed by Bullock, Imai, and Shapiro (2011) <DOI:10.1093/pan/mpr031> to analyze endorsement experiments.  Endorsement experiments are a survey methodology for eliciting truthful responses to sensitive questions.  This methodology is helpful when measuring support for socially sensitive political actors such as militant groups.  The model is fitted with a Markov chain Monte Carlo algorithm and produces the output containing draws from the posterior distribution. 
	"""
	
	homepage = "https://github.com/SensitiveQuestions/endorse/"
	cran = "endorse" 

	version("1.6.2", md5="29c1ab9e87b8e21f6f16174e4c05ef1a")

	depends_on("r-coda", type=("build", "run"))
