# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinypanels(RPackage):
	"""Shiny Layout with Collapsible Panels

	Create 'Shiny Apps' with collapsible vertical panels. 
    This package provides a new visual arrangement for elements on top of 'Shiny'. 
    Use the expand and collapse capabilities to leverage web applications with
    many elements to focus the user attention on the panel of interest.
	"""
	
	homepage = "http://github.com/datasketch/shinypanels"
	cran = "shinypanels" 

	version("0.5.0", md5="9bc075bdb94997e07c8119ecb838415b")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
