# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocknitr(RPackage):
	"""Use Docker Images to Process Rmarkdown Blocks

	Gives you the ability to use arbitrary Docker images
    (including custom ones) to process Rmarkdown code chunks.
	"""
	
	cran = "docknitr" 

	version("1.0.1", md5="a8cb09efc80e79cac005457d457e4dde")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-sys", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
