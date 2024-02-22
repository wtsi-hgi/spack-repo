# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecastcombinations(RPackage):
	"""Forecast Combinations

	Aim: Supports the most frequently used methods to combine forecasts. Among others: Simple average, Ordinary Least Squares, Least Absolute Deviation, Constrained Least Squares, Variance-based, Best Individual model, Complete subset regressions and Information-theoretic (information criteria based).
	"""
	
	cran = "ForecastCombinations" 

	version("1.1", md5="18d98ce7c0e18c252f903e01298fd967")

	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
