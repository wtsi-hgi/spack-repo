# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfortify(RPackage):
	"""Data Visualization Tools for Statistical Analysis Results

	Unified plotting tools for statistics commonly used, such as GLM,
    time series, PCA families, clustering and survival analysis. The package offers
    a single plotting interface for these analysis results and plots in a unified
    style using 'ggplot2'.
	"""
	
	homepage = "https://github.com/sinhrks/ggfortify"
	cran = "ggfortify" 

	version("0.4.16", md5="6e788d8cdd6a50880ca9cb2094f1ca9f")

	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-dplyr@0.3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
