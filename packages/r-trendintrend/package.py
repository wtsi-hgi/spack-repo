# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendintrend(RPackage):
	"""Odds Ratio Estimation and Power Calculation for the Trend in
Trend Model

	Estimation of causal odds ratio and power calculation given trends in exposure prevalence    and outcome frequencies of stratified data.
	"""
	
	cran = "TrendInTrend" 

	version("1.1.3", md5="1beb4fe7528df4e81e486e40a838e51e")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
