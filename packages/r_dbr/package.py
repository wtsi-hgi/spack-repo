# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbr(RPackage):
	"""Discrete Beta Regression

	Bayesian Beta Regression, adapted for bounded discrete responses, commonly seen in survey responses.
  Estimation is done via Markov Chain Monte Carlo sampling, using a Gibbs wrapper around univariate slice sampler 
  (Neal (2003) <DOI:10.1214/aos/1056562461>), as implemented in the R package MfUSampler 
  (Mahani and Sharabiani (2017) <DOI: 10.18637/jss.v078.c01>).
	"""
	
	cran = "DBR" 

	version("1.4.1", md5="270ef4883d0e44f6a97d8809abd1736f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mfusampler", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
