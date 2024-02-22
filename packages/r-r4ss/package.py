# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR4ss(RPackage):
	"""R Code for Stock Synthesis

	A collection of R functions for use with Stock Synthesis, a
    fisheries stock assessment modeling platform written in ADMB by Dr. Richard
    D. Methot at the NOAA Northwest Fisheries Science Center. The functions
    include tools for summarizing and plotting results, manipulating files,
    visualizing model parameterizations, and various other common stock
    assessment tasks.
    This version of '{r4ss}' is compatible with Stock Synthesis versions
    3.24 through 3.30 (specifically version 3.30.19.01, from April
    2022).
	"""
	
	homepage = "https://github.com/r4ss/r4ss"
	cran = "r4ss" 

	version("1.44.0", md5="37ae5d02f64c684a39a42e14ff237301")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
