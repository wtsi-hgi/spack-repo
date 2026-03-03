# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevealjs(RPackage):
	"""R Markdown Format for 'reveal.js' Presentations

	R Markdown format for 'reveal.js' presentations, a framework 
  for easily creating beautiful presentations using HTML.
	"""
	
	homepage = "https://github.com/rstudio/revealjs"
	cran = "revealjs" 

	version("0.9", md5="69b18803a1dbc7f775a9912b1029d096")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rmarkdown@1:", type=("build", "run"))
