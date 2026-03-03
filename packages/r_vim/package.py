# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVim(RPackage):
	"""Visualization and Imputation of Missing Values

	New tools for the visualization of missing and/or imputed values
    are introduced, which can be used for exploring the data and the structure of
    the missing and/or imputed values. Depending on this structure of the missing
    values, the corresponding methods may help to identify the mechanism generating
    the missing values and allows to explore the data including missing values.
    In addition, the quality of imputation can be visually explored using various
    univariate, bivariate, multiple and multivariate plot methods. A graphical user
    interface available in the separate package VIMGUI allows an easy handling of
    the implemented plot methods.
	"""
	
	homepage = "https://github.com/statistikat/VIM"
	cran = "VIM" 

	version("6.2.2", md5="4dc9bb7baa02b064e9cd2d994092fbb8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-laeken", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-data-table@1.9.4:", type=("build", "run"))
