# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBekks(RPackage):
	"""Multivariate Conditional Volatility Modelling and Forecasting

	Methods and tools for estimating, simulating and forecasting of so-called BEKK-models (named after Baba, Engle, Kraft and Kroner) based on the fast Berndt–Hall–Hall–Hausman (BHHH) algorithm described in Hafner and Herwartz (2008) <doi:10.1007/s00184-007-0130-y>. 
	"""
	
	cran = "BEKKs" 

	version("1.4.4", md5="920c9a4ba72e2863bb8f4152881d3916")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-gas", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
