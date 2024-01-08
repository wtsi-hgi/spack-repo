# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RGdtools(RPackage):
	"""Utilities for Graphical Rendering and Fonts Management

	Tools are provided to compute metrics of 
  formatted strings and to check the availability of a font. 
  Another set of functions is provided to support the collection 
  of fonts from 'Google Fonts' in a cache. Their use is simple within 
  'R Markdown' documents and 'shiny' applications but also with graphic 
  productions generated with the 'ggiraph', 'ragg' and 'svglite' packages 
  or with tabular productions from the 'flextable' package.
	"""
	
	homepage = "https://davidgohel.github.io/gdtools/"
	cran = "gdtools" 

	version("0.3.4", md5="4c55822c259bca2c93f1ed604199e0c6")

	depends_on("r@4.0.0:", type=("build", "run"))
	depends_on("r-rcpp@0.12.12:", type=("build", "run"))
	depends_on("r-systemfonts@0.1.1:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-gfonts", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-fontquiver@0.2.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

	depends_on("cairo+ft", type=("build", "link"))
	depends_on("freetype", type=("build", "link"))
	depends_on("fontconfig", type=("build", "link"))
	depends_on("pkg-config")

