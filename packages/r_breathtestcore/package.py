# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreathtestcore(RPackage):
	"""Core Functions to Read and Fit 13c Time Series from Breath Tests

	Reads several formats of 13C data (IRIS/Wagner,
    BreathID) and CSV.  Creates artificial sample data for testing.  Fits
    Maes/Ghoos, Bluck-Coward self-correcting formula using 'nls', 'nlme'.
    Methods to fit breath test curves with Bayesian Stan methods are
    refactored to package 'breathteststan'. For a Shiny GUI, see package
    'dmenne/breathtestshiny' on github.
	"""
	
	homepage = "https://github.com/dmenne/breathtestcore"
	cran = "breathtestcore" 

	version("0.8.7", md5="cceceb3167f120879ee7bfb7ba66aad2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-broom@0.7:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
