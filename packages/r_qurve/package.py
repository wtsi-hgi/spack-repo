# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQurve(RPackage):
	"""Robust and User-Friendly Analysis of Growth and Fluorescence
Curves

	High-throughput analysis of growth curves and fluorescence
    data using three methods: linear regression, growth model fitting, and
    smooth spline fit. Analysis of dose-response relationships via
    smoothing splines or dose-response models. Complete data analysis
    workflows can be executed in a single step via user-friendly wrapper
    functions. The results of these workflows are summarized in detailed
    reports as well as intuitively navigable 'R' data containers. A 'shiny'
    application provides access to all features without
    requiring any programming knowledge. The package is described in further
    detail in Wirth et al. (2023) <doi:10.1038/s41596-023-00850-7>.
	"""
	
	homepage = "https://github.com/NicWir/QurvE"
	cran = "QurvE" 

	version("1.1.1", md5="abf8cdc370bea0e4b59de0482ec9ff95")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
