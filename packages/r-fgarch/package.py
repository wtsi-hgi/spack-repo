# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgarch(RPackage):
	"""Rmetrics - Autoregressive Conditional Heteroskedastic Modelling

	Analyze and model heteroskedastic behavior in financial time series.
	"""
	
	homepage = "https://geobosh.github.io/fGarchDoc/"
	cran = "fGarch" 

	version("4032.91", md5="ca15ab94fce373d17770107377efe8f8")
	version("4033.92", md5="c61344e53fcc68b80936d7b46d376a44")

	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-fastica", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-cvar@0.5:", type=("build", "run"))
