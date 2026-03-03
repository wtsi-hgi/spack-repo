# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLightparser(RPackage):
	"""From 'Rmarkdown' and 'Quarto' Files to Tibble and Back

	Split your 'rmarkdown' or 'quarto' files by sections into a
    tibble: titles, text, chunks. Rebuild the file from the tibble.
	"""
	
	homepage = "https://github.com/ThinkR-open/lightparser"
	cran = "lightparser" 

	version("0.1.0", md5="b3d44d8765e46cca17fb1948915b386f")

	depends_on("r-knitr@1.35:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
