# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArtpack(RPackage):
	"""Creates Generative Art Data

	Create data that displays generative art when mapped into a 'ggplot2' plot. Functionality includes specialized data frame creation for geometric shapes, tools that define artistic color palettes, tools for geometrically transforming data, and other miscellaneous tools that are helpful when using 'ggplot2' for generative art.
	"""
	
	homepage = "https://meghansaha.github.io/artpack/"
	cran = "artpack" 

	version("0.1.0", md5="a0b056c7bd5c1342cad3aca3b2441835")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-tibble@3.1.6:", type=("build", "run"))
