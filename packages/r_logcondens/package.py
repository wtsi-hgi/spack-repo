# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogcondens(RPackage):
	"""Estimate a Log-Concave Probability Density from Iid Observations

	Given independent and identically distributed observations X(1), ..., X(n), compute the maximum likelihood estimator (MLE) of a density as well as a smoothed version of it under the assumption that the density is log-concave, see Rufibach (2007) and Duembgen and Rufibach (2009). The main function of the package is 'logConDens' that allows computation of the log-concave MLE and its smoothed version. In addition, we provide functions to compute (1) the value of the density and distribution function estimates (MLE and smoothed) at a given point (2) the characterizing functions of the estimator, (3) to sample from the estimated distribution, (5) to compute a two-sample permutation test based on log-concave densities, (6) the ROC curve based on log-concave estimates within cases and controls, including confidence intervals for given values of false positive fractions (7) computation of a confidence interval for the value of the true density at a fixed point. Finally, three datasets that have been used to illustrate log-concave density estimation are made available.
	"""
	
	homepage = "http://www.kasparrufibach.ch"
	cran = "logcondens" 

	version("2.1.8", md5="32c2696b983852fd3521a1f0fd2bcbdc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
