# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSjplot(RPackage):
	"""Data Visualization for Statistics in Social Science

	Collection of plotting and table output functions for data
    visualization. Results of various statistical analyses (that are commonly used
    in social sciences) can be visualized using this package, including simple and
    cross tabulated frequencies, histograms, box plots, (generalized) linear models,
    mixed effects models, principal component analysis and correlation matrices, 
    cluster analyses, scatter plots, stacked scales, effects plots of regression 
    models (including interaction terms) and much more. This package supports
    labelled data.
	"""
	
	homepage = "https://strengejacke.github.io/sjPlot/"
	cran = "sjPlot" 

	version("2.8.15", md5="2ed1dc993db5e6e1e2e74e6df993fe13")
	version("2.8.14", md5="d751cfa9c29b4519bb6bb1133adc8061")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-datawizard", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggeffects", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-parameters", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sjlabelled@1.1.2:", type=("build", "run"))
	depends_on("r-sjmisc@2.8.2:", type=("build", "run"))
	depends_on("r-sjstats@0.17.8:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
