# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBscui(RPackage):
	"""Build SVG Custom User Interface

	Render SVG as interactive figures to display contextual
   information, with selectable and clickable user interface elements.
   These figures can be seamlessly integrated into 'rmarkdown' and 'Quarto'
   documents, as well as 'shiny' applications, allowing manipulation of elements
   and reporting actions performed on them.
   Additional features include pan, zoom in/out functionality, and the ability
   to export the figures in SVG or PNG formats.
	"""
	
	homepage = "https://patzaw.github.io/bscui/"
	cran = "bscui" 

	version("0.1.5", md5="d13c1c76b47ae5f026834d5fbe5ce790")
	version("0.1.3", md5="1f3a16d6c6c2a5a1e093c0b054224b09")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-webshot2", type=("build", "run"))
