# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgstats(RPackage):
	"""Extension to 'ggplot2' for Plotting Stats

	Provides new statistics, new geometries and new positions for 
	'ggplot2' and a suite of functions to facilitate the creation of 
	statistical plots.
	"""
	
	homepage = "https://larmarange.github.io/ggstats/"
	cran = "ggstats" 

	version("0.13.0", sha256="82dd03ca8dd49baa5567b54a25c749516800574b008d61e63e95efc6c87cd787")
	version("0.12.0", sha256="1fcd1b429a487fc083cf0348e73b2cd4075ca6a6976edcd71b73326bdd36fdbd")
	version("0.11.0", sha256="6e5246e95611606ba334769cf58267a92fa36104f8af74005be0b5602501b708")
	version("0.10.0", sha256="c6cf36dc97f7d782d0507e901618c865a4e588ff1dbafd2f33cbd583ce3fd717")
	version("0.9.0", sha256="610f3779fdef48795b04e9cd85e33a62c43fd4b7147cc429b13b1f96594f0c84")
	version("0.8.0", sha256="6a53c2f4d4ac35d12b02d75cea38507fb13a33dad479abbcd9dfc5a7ee869c23")
	version("0.7.0", sha256="e84cc52892c0e4f13a2700b448a589f6ecc816e7cf7cf5c2b4c1310d02d9f980")
	version("0.6.0", sha256="f80aaa229f542cb18174b9ab82b0026c6bd3331f22bf2662712ab6af480b6d80")
	version("0.5.1", md5="d615412a8c42e91abadd45f5d88c49a0")

	depends_on("r-broom-helpers@1.14:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@4:", type=("build", "run"), when="@0.9.0:")
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
