# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbcc(RPackage):
	"""Risk-Based Control Charts

	Univariate and multivariate versions of risk-based control charts. Univariate versions of control charts, such as the risk-based version of X-bar, Moving Average (MA), Exponentially Weighted Moving Average Control Charts (EWMA), and Cumulative Sum Control Charts (CUSUM) charts. The risk-based version of the multivariate T2 control chart. Plot and summary functions. Kosztyan et. al. (2016) <doi:10.1016/j.eswa.2016.06.019>.
	"""
	
	homepage = "https://github.com/kzst/rbcc"
	cran = "rbcc" 

	version("0.1.0", md5="393876a4a82b95e9b13b17f7c7ebfd8c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-qcc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-pearsonds", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
