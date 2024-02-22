# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTufte(RPackage):
	"""Tufte's Styles for R Markdown Documents

	Provides R Markdown output formats to use Tufte styles for
    PDF and HTML output.
	"""
	
	homepage = "https://github.com/rstudio/tufte"
	cran = "tufte" 

	version("0.13", md5="bc40d5df8f6e7f0e20fd11db2b4bcad7")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr@1.28:", type=("build", "run"))
	depends_on("r-rmarkdown@2.11:", type=("build", "run"))
	depends_on("r-xfun@0.13:", type=("build", "run"))
