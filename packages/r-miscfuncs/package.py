# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiscfuncs(RPackage):
	"""Miscellaneous Useful Functions Including LaTeX Tables, Kalman
Filtering, QQplots with Simulation-Based Confidence Intervals
and Development Tools

	Implementing various things including functions for LaTeX tables,
    the Kalman filter, QQ-plots with simulation-based confidence intervals, web scraping, development tools, relative risk and odds
    ratio.
	"""
	
	cran = "miscFuncs" 

	version("1.5-7", md5="69d95c47afaf8db7bfed7446c88bb67c")

	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
