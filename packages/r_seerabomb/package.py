# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeerabomb(RPackage):
	"""SEER and Atomic Bomb Survivor Data Analysis Tools

	Creates SEER (Surveillance, Epidemiology and End Results) and 
    A-bomb data binaries from ASCII sources and provides tools for estimating
    SEER second cancer risks. Methods are described in <doi:10.1038/leu.2015.258>.
	"""
	
	homepage = "http://epbi-radivot.cwru.edu/SEERaBomb/SEERaBomb.html"
	cran = "SEERaBomb" 

	version("2019.2", md5="e3ac3ced9b9b619e8c80f300c55941a9")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-demography", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-laf", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
