# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2resize(RPackage):
	"""In-Text Resizer for Images, Tables and Fancy Resizable
Containers in 'shiny', 'rmarkdown' and 'quarto' Documents

	Automatic resizing toolbar for containers, images and tables. Various resizable or expandable container functionalities are also included. Most suitable to include in 'shiny', 'markdown' and 'quarto' documents.
	"""
	
	homepage = "https://r2resize.obi.obianom.com"
	cran = "r2resize" 

	version("1.9", md5="ce948382699bc1fb17181dac46f44ce4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-quickcode", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-nextgenshinyapps", type=("build", "run"))
