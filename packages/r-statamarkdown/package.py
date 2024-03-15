# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatamarkdown(RPackage):
	"""'Stata' Markdown

	Settings and functions to extend the 'knitr' 'Stata' engine.
	"""
	
	cran = "Statamarkdown" 

	version("0.9.2", md5="e341f0f9ce47c66473318bf853afa7b1")

	depends_on("r-knitr@1.43:", type=("build", "run"))
	depends_on("r-xfun@0.39:", type=("build", "run"))
	depends_on("stata", type=("build", "link", "run"))
