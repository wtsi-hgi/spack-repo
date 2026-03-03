# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerformanceanalytics(RPackage):
	"""Econometric Tools for Performance and Risk Analysis

	Collection of econometric functions for performance and risk 
    analysis. In addition to standard risk and performance metrics, this 
    package aims to aid practitioners and researchers in utilizing the latest
    research in analysis of non-normal return streams.  In general, it is most 
    tested on return (rather than price) data on a regular scale, but most 
    functions will work with irregular return data as well, and increasing
    numbers of functions will work with P&L or price data where possible.
	"""
	
	homepage = "https://github.com/braverock/PerformanceAnalytics"
	cran = "PerformanceAnalytics" 

	version("2.0.4", md5="d6980fbdf785e993e1f1d1c3121f36ab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xts@0.10:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
