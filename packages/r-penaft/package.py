# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenaft(RPackage):
	"""Fit the Regularized Gehan Estimator with Elastic Net and Sparse
Group Lasso Penalties

	The semiparametric accelerated failure time (AFT) model is an attractive alternative to the Cox proportional hazards model. This package provides a suite of functions for fitting one popular estimator of the semiparametric AFT model, the regularized Gehan estimator. Specifically, we provide functions for cross-validation, prediction, coefficient extraction, and visualizing both trace plots and cross-validation curves. For further details, please see Suder, P. M. and Molstad, A. J., (2022+) Scalable algorithms for semiparametric accelerated failure time models in high dimensions, to appear in Statistics in Medicine <doi:10.1002/sim.9264>. 
	"""
	
	homepage = "ajmolstad.github.io/research"
	cran = "penAFT" 

	version("0.3.0", md5="cbd48b336c7ec47994c3f0cdfe32618b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
