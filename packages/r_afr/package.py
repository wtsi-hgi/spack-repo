# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfr(RPackage):
	"""Toolkit for Regression Analysis of Kazakhstan Banking Sector
Data

	Tool is created for regression, prediction and forecast analysis of macroeconomic and credit data.
  The package includes functions from existing R packages adapted for banking sector of Kazakhstan.
  The purpose of the package is to optimize statistical functions for easier interpretation for bank analysts and non-statisticians.
	"""
	
	cran = "AFR"

	version("0.3.5", md5="e1e191de086f4b4a73e23ec793ba8301")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-olsrr", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
