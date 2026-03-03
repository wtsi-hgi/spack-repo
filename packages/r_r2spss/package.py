# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2spss(RPackage):
	"""Format R Output to Look Like SPSS

	Create plots and LaTeX tables that look like SPSS output for use in teaching materials.  Rather than copying-and-pasting SPSS output into documents, R code that mocks up SPSS output can be integrated directly into dynamic LaTeX documents with tools such as knitr.  Functionality includes statistical techniques that are typically covered in introductory statistics classes: descriptive statistics, common hypothesis tests, ANOVA, and linear regression, as well as box plots, histograms, scatter plots, and line plots (including profile plots).
	"""
	
	homepage = "https://github.com/aalfons/r2spss"
	cran = "r2spss" 

	version("0.3.2", md5="5cc1cc7c2f496d4700696dc7a0accff3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
