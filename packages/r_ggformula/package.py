# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgformula(RPackage):
	"""Formula Interface to the Grammar of Graphics

	Provides a formula interface to 'ggplot2' graphics.
	"""
	
	homepage = "https://github.com/ProjectMOSAIC/ggformula"
	cran = "ggformula" 

	version("0.12.0", md5="8eee6fba1dc5081b680ecd4ae73c42b4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-mosaiccore@0.7:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
