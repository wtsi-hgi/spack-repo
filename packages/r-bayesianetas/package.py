# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianetas(RPackage):
	"""Bayesian Estimation of the ETAS Model for Earthquake Occurrences

	The Epidemic Type Aftershock Sequence  (ETAS) model is one of the best-performing methods for modeling and forecasting earthquake occurrences. This package implements Bayesian estimation routines to draw samples from the full posterior distribution of the model parameters, given an earthquake catalog. The paper on which this package is based is Gordon J. Ross - Bayesian Estimation of the ETAS Model for Earthquake Occurrences (2016), available from the below URL.
	"""
	
	homepage = "http://www.gordonjross.co.uk/bayesianetas.pdf"
	cran = "bayesianETAS" 

	version("1.0.3", md5="243da82359ca4b3d0c9332e34be650d6")

	depends_on("r@2.15:", type=("build", "run"))
