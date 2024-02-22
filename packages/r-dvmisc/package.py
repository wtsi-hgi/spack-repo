# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDvmisc(RPackage):
	"""Convenience Functions, Moving Window Statistics, and Graphics

	Contains functions that do something convenient (e.g. create BMI categories), functions for calculating moving-window statistics efficiently, and functions for generating various figures (e.g. histograms with fitted probability mass/density function).
	"""
	
	cran = "dvmisc" 

	version("1.1.4", md5="b9ff121a86cf0d8860d9b475a1798102")

	depends_on("r-rbenchmark", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-tab", type=("build", "run"))
