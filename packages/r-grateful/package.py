# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrateful(RPackage):
	"""Facilitate Citation of R Packages

	Facilitates the citation of R packages used in analysis
    projects. Scans project for packages used, gets their citations, and
    produces a document with citations in the preferred bibliography
    format, ready to be pasted into reports or manuscripts. Alternatively,
    'grateful' can be used directly within an 'R Markdown' or 'Quarto' document.
	"""
	
	homepage = "https://pakillo.github.io/grateful/"
	cran = "grateful" 

	version("0.2.4", md5="2bd1b42c25f275171542aa9b6f4c43dd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
