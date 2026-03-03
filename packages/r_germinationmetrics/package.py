# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGerminationmetrics(RPackage):
	"""Seed Germination Indices and Curve Fitting

	Provides functions to compute various germination indices
    such as germinability, median germination time, mean germination time,
    mean germination rate, speed of germination, Timson's index,
    germination value, coefficient of uniformity of germination,
    uncertainty of germination process, synchrony of germination etc. from
    germination count data. Includes functions for fitting cumulative seed
    germination curves using four-parameter hill function and computation
    of associated parameters. See the vignette for more, including full
    list of citations for the methods implemented.
	"""
	
	homepage = "https://github.com/aravind-j/germinationmetrics"
	cran = "germinationmetrics" 

	version("0.1.8", md5="5e8b28eb11bfbfdc4c5f2fafff13dc02")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-gslnls", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
