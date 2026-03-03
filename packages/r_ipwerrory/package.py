# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpwerrory(RPackage):
	"""Inverse Probability Weighted Estimation of Average Treatment
Effect with Misclassified Binary Outcome

	An implementation of the correction methods proposed by Shu and Yi (2017) <doi:10.1177/0962280217743777> for the inverse probability weighted (IPW) estimation of average treatment effect (ATE) with misclassified binary outcomes. Logistic regression model is assumed for treatment model for all implemented correction methods, and is assumed for the outcome model for the implemented doubly robust correction method. Misclassification probability given a true value of the outcome is assumed to be the same for all individuals.
	"""
	
	cran = "ipwErrorY" 

	version("2.1", md5="e9c12aa61870aefcc2c3686fd389f285")

	depends_on("r-nleqslv", type=("build", "run"))
