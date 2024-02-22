# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharperratio(RPackage):
	"""Moment-Free Estimation of Sharpe Ratios

	An efficient moment-free estimator of the Sharpe ratio, or signal-to-noise ratio, for heavy-tailed data (see <arXiv:1505.01333>).
	"""
	
	cran = "sharpeRratio" 

	version("1.4.3", md5="31ac7b26d4b21938cabaaec80c465fc3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ghyp", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
