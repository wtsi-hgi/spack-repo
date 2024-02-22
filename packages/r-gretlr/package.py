# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGretlr(RPackage):
	"""A Seamless Integration of 'Gretl' and 'R'

	It allows running 'gretl' (<http://gretl.sourceforge.net/index.html>) program from R, R Markdown and Quarto. 'gretl' ('Gnu' Regression, 'Econometrics', and Time-series Library) is a statistical software for Econometric analysis.  This package does not only integrate 'gretl' and 'R' but also serves  as a 'gretl' Knit-Engine for 'knitr' package. Write all your 'gretl' commands in 'R', R Markdown chunk.
	"""
	
	homepage = "https://CRAN.R-project.org/package=gretlR"
	cran = "gretlR" 

	version("0.1.4", md5="73b59799f7c26687bc79b13aac3e9139")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
