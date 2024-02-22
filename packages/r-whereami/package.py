# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhereami(RPackage):
	"""Reliably Return the Source and Call Location of a Command

	Robust and reliable functions to return informative outputs to 
        console with the run or source location of a command. This can be from
        the  'RScript'/R terminal commands or 'RStudio' console, source editor, 
        'Rmarkdown' document and a Shiny application.
	"""
	
	homepage = "https://github.com/yonicd/whereami"
	cran = "whereami" 

	version("0.2.0", md5="f3c29461c8375a5f57664f12e0e5dc93")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
