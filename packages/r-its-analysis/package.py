# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItsAnalysis(RPackage):
	"""Running Interrupted Time Series Analysis

	Two functions for running and then post-estimating an Interrupted Time Series Analysis model. This is a solution for running time series analyses on temporally short data. See English (2019) 'The its.analysis R package - Modelling short time series data' <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3398189> for an overview of the method.
	"""
	
	cran = "its.analysis" 

	version("1.6.0", md5="d02a94b44aab31743cae234d268a5fbe")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
