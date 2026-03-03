# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmdpartials(RPackage):
	"""Partial 'rmarkdown' Documents to Prettify your Reports

	
		Use 'rmarkdown' partials, also know as child documents in
		'knitr', so you can make components for HTML, PDF, and Word documents. 
		The package provides various helper functions to make certain functions easier. 
		You may want to use this package, if you want to flexibly summarise objects 
		using a combination of figures, tables, text, and HTML widgets. 
		Unlike HTML widgets, the output is Markdown and can hence be turn into other
		output formats than HTML.
	"""
	
	homepage = "https://github.com/rubenarslan/rmdpartials"
	cran = "rmdpartials" 

	version("0.5.8", md5="ee6a3dd1cb4123c58717aa0ac12b6389")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
