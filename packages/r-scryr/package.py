# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScryr(RPackage):
	"""An Interface to the 'Scryfall' API

	A simple, light, and robust interface between R and
    the 'Scryfall' card data API <https://scryfall.com/docs/api>.
	"""
	
	homepage = "https://curso-r.github.io/scryr/"
	cran = "scryr" 

	version("1.0.0", md5="acabd7f8cc6f43994f3064190943eec6")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
