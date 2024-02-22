# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymbolEquationGpt(RPackage):
	"""Powerful User Interface to Build Equations and Add Symbols

	User Interface for adding symbols, smileys, arrows, building mathematical equations using 'LaTeX' or 'r2symbols'. Built for use in development of 'Markdown' and 'Shiny' Outputs.
	"""
	
	homepage = "https://symbols-ui.obi.obianom.com"
	cran = "symbol.equation.gpt" 

	version("1.1.3", md5="3d208962dbd26261cff7b52cce3620d6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-nextgenshinyapps", type=("build", "run"))
	depends_on("r-r2symbols", type=("build", "run"))
	depends_on("r-shinystoreplus", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
