# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpbayes(RPackage):
	"""Tools for Gaussian Process Modeling in Uncertainty
Quantification

	Gaussian processes ('GPs') have been widely used to model spatial data, 'spatio'-temporal data, and computer experiments in diverse areas of statistics including spatial statistics, 'spatio'-temporal statistics, uncertainty quantification, and machine learning. This package creates basic tools for fitting and prediction based on 'GPs' with spatial data, 'spatio'-temporal data, and computer experiments. Key characteristics for this GP tool include: (1) the comprehensive implementation of various covariance functions including the 'Matérn' family and the Confluent 'Hypergeometric' family with isotropic form, tensor form, and automatic relevance determination form, where the isotropic form is widely used in spatial statistics, the tensor form is widely used in design and analysis of computer experiments and uncertainty quantification, and the automatic relevance determination form is widely used in machine learning; (2) implementations via Markov chain Monte Carlo ('MCMC') algorithms and optimization algorithms for GP models with all the implemented covariance functions. The methods for fitting and prediction are mainly implemented in a Bayesian framework; (3) model evaluation via Fisher information and predictive metrics such as predictive scores; (4) built-in functionality for simulating 'GPs' with all the implemented covariance functions; (5) unified implementation to allow easy specification of various 'GPs'. 
	"""
	
	cran = "GPBayes" 

	version("0.1.0-5.1", md5="adf1cd3c4343409ee88c9811c53677c5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("gsl@2.5:", type=("build", "link", "run"))
