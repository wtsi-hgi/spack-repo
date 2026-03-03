# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtemps(RPackage):
	"""R Templates for Reproducible Data Analyses

	A collection of R Markdown templates for nicely structured, reproducible 
    data analyses in R. The templates have embedded examples on how to write 
    citations, footnotes, equations and use colored message/info boxes, how to 
    cross-reference different parts/sections in the report, provide a nice 
    table of contents (toc) with a References section and proper R session 
    information as well as examples using DT tables and ggplot2 graphs. 
    The bookdown Lite template theme supports code folding.
	"""
	
	homepage = "https://github.com/bblodfon/rtemps"
	cran = "rtemps" 

	version("0.8.0", md5="a9dadf86c2d93906e943639a9dfc0c20")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
