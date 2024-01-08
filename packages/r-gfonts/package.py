# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RGfonts(RPackage):
	"""Offline 'Google' Fonts for 'Markdown' and 'Shiny'

	Download 'Google' fonts and generate 'CSS' to use in 'rmarkdown' documents and 
  'shiny' applications. Some popular fonts are included and ready to use.
	"""
	
	homepage = "https://dreamrs.github.io/gfonts/"
	cran = "gfonts" 

	version("0.2.0", md5="2a3cb33c1a2d0053f2a8ddad6ba0e2de")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
