# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RGgprism(RPackage):
	"""A 'ggplot2' Extension Inspired by 'GraphPad Prism'

	Provides various themes, palettes, and other functions
    that are used to customise ggplots to look like they were made in 'GraphPad 
    Prism'. The 'Prism'-look is achieved with theme_prism() and 
    scale_fill|colour_prism(), axes can be changed with custom guides like 
    guide_prism_minor(), and significance indicators added with add_pvalue().
	"""
	
	homepage = "https://csdaw.github.io/ggprism/"
	cran = "ggprism" 

	version("1.0.4", md5="e42b006be945f80d62dc240066e15244")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ggplot2@3.2.0:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gtable@0.1.1:", type=("build", "run"))
	depends_on("r-rlang@0.3.0:", type=("build", "run"))
	depends_on("r-scales@0.5.0:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
