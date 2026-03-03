# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStructuraldecompose(RPackage):
	"""Decomposes a Level Shifted Time Series

	Explains the behavior of a time series by decomposing it into its trend, seasonality and residuals. 
             It is built to perform very well in the presence of significant level shifts. It is designed to play 
             well with any breakpoint algorithm and any smoothing algorithm. Currently defaults to 'lowess' for smoothing
             and 'strucchange' for breakpoint identification. The package is useful in areas such as trend analysis, time series 
             decomposition, breakpoint identification and anomaly detection.
	"""
	
	homepage = "https://allen-1242.github.io/StructuralDecompose/"
	cran = "StructuralDecompose" 

	version("0.1.1", md5="6495b0a7bf83b150407e8fe1b199eb5e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
