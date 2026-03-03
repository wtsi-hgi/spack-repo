# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinynorrrm(RPackage):
	"""The Ultimate Igneous Norm

	The computer program is an efficient igneous norm algorithm and rock classification system written in R but run as shiny app.
	"""
	
	homepage = "https://github.com/TheRFrog/shinyNORRRM"
	cran = "shinyNORRRM" 

	version("0.8.6", md5="4a0d44010cfcfd86d67366813a8b5fca")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ternary", type=("build", "run"))
