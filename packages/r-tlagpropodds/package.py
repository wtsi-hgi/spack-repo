# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTlagpropodds(RPackage):
	"""Proportional Odds Model with Censored, Time-Lagged Categorical
Outcome

	Implements a semiparametric estimator for the odds ratio model with
    censored, time-lagged, ordered categorical outcome in a randomized clinical
    trial that incorporates baseline and time-dependent information. 
    Tsiatis, A. A. and Davidian, M. (2021) <arXiv:2106.15559>.
	"""
	
	cran = "tLagPropOdds" 

	version("1.9", md5="b3261af3dcba1cd8c71ff04305fa9411")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
