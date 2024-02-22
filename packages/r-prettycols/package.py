# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrettycols(RPackage):
	"""Pretty Colour Palettes

	Defines aesthetically pleasing colour palettes.
	"""
	
	homepage = "https://nrennie.github.io/PrettyCols/"
	cran = "PrettyCols" 

	version("1.0.1", md5="9e849db64bcacca2d03cb1f1380c6a66")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
