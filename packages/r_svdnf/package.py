# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvdnf(RPackage):
	"""Discrete Nonlinear Filtering for Stochastic Volatility Models

	Generates simulated paths from various financial stochastic volatility models
 with jumps and applies the discrete nonlinear filter (DNF) of Kitagawa (1987) <doi:10.1080/01621459.1987.10478534> to 
 compute likelihood evaluations, filtering distribution estimates, and maximum likelihood parameter estimates.
 The algorithm is implemented following the work of Bégin and Boudreault (2021) <doi:10.1080/10618600.2020.1840995>.
	"""
	
	cran = "SVDNF" 

	version("0.1.8", md5="c0229828fe470b983eb5cfe771a5be37")

	depends_on("r-rcpp", type=("build", "run"))
