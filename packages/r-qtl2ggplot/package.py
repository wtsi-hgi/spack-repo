# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtl2ggplot(RPackage):
	"""Data Visualization for QTL Experiments

	Functions to plot QTL (quantitative trait loci) analysis
    results and related diagnostics.
    Part of 'qtl2', an upgrade of the 'qtl'
    package to better handle high-dimensional data and complex cross
    designs.
	"""
	
	homepage = "https://github.com/byandell/qtl2ggplot"
	cran = "qtl2ggplot" 

	version("1.2.4", md5="501a59ea4e76fcca22a999f964340f82")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-qtl2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
