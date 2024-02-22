# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlipdownr(RPackage):
	"""Implement a Countdown in 'RMarkdown' Documents and 'shiny'
Applications

	Allows the user to create a countdown in 'RMarkdown' documents and 'shiny' applications. 
    The package is a wrapper of the 'JavaScript' library 'flipdown.js'. See <https://pbutcher.uk/flipdown/> for more info.
	"""
	
	homepage = "https://github.com/feddelegrand7/flipdownr"
	cran = "flipdownr" 

	version("0.1.1", md5="7c7717fcfed1b12e8de86d59f737bf47")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
