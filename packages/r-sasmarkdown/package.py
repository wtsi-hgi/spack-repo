# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSasmarkdown(RPackage):
	"""'SAS' Markdown

	Settings and functions to extend the 'knitr' 'SAS' engine.
	"""
	
	homepage = "https://www.ssc.wisc.edu/~hemken/SASworkshops/sas.html#writing-sas-documentation"
	cran = "SASmarkdown" 

	version("0.8.2", md5="17b36f26316758b60e2fbab259a13646")

	depends_on("r-knitr@1.21:", type=("build", "run"))
	depends_on("r-xfun@0.4:", type=("build", "run"))
