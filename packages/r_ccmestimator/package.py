# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcmestimator(RPackage):
	"""Comparative Causal Mediation Estimation

	Functions to perform comparative causal mediation analysis to compare the mediation effects of different treatments via a common mediator. Results contain the estimates and confidence intervals for the two comparative causal mediation analysis estimands, as well as the ATE and ACME for each treatment. Functions provided in the package will automatically assess the comparative causal mediation analysis scope conditions (i.e. for each comparative causal mediation estimand, a numerator and denominator that are both estimated with the desired statistical significance and of the same sign). Results will be returned for each comparative causal mediation estimand only if scope conditions are met for it. See details in Bansak(2020)<doi:10.1017/pan.2019.31>.
	"""
	
	homepage = "https://github.com/xiw021/ccmEstimator"
	cran = "ccmEstimator" 

	version("1.0.0", md5="9a05787a581079e6c9e6b45dd5efacfd")

	depends_on("r@2.10:", type=("build", "run"))
