# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBurnr(RPackage):
	"""Forest Fire History Analysis

	Tools to read, write, parse, and analyze forest fire history data (e.g. FHX). Described in Malevich et al. (2018) <doi:10.1016/j.dendro.2018.02.005>.
	"""
	
	homepage = "https://github.com/ltrr-arizona-edu/burnr/"
	cran = "burnr" 

	version("0.6.1", md5="01f025380b3379c8107b7b12ee5ad585")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
