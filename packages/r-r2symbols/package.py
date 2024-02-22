# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2symbols(RPackage):
	"""Symbols for 'Markdown' and 'Shiny' Application

	Direct insertion of over 1000 symbols (e.g. currencies, letters, emojis, arrows, mathematical symbols and so on) into 'Rmarkdown' documents and 'Shiny' applications by incorporating 'HTML' hex codes.
	"""
	
	homepage = "https://r2symbols.obi.obianom.com"
	cran = "r2symbols" 

	version("1.4", md5="68cac7f1ca86ff2e27d5acc11297cc18")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
