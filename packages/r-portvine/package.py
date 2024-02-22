# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortvine(RPackage):
	"""Vine Based (Un)Conditional Portfolio Risk Measure Estimation

	Following Sommer (2022) <https://mediatum.ub.tum.de/1658240>
    portfolio level risk estimates (e.g. Value at Risk, Expected
    Shortfall) are estimated by modeling each asset univariately by an
    ARMA-GARCH model and then their cross dependence via a Vine Copula
    model in a rolling window fashion. One can even condition on
    variables/time series at certain quantile levels to stress test the
    risk measure estimates.
	"""
	
	homepage = "https://github.com/EmanuelSommer/portvine"
	cran = "portvine" 

	version("1.0.3", md5="3698f4115c6aa0f2ae2b9e2657929cb0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dtplyr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-rvinecopulib", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-kde1d", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
	depends_on("r-wdm", type=("build", "run"))
