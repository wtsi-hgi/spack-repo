# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtextras(RPackage):
	"""Extending 'gt' for Beautiful HTML Tables

	Provides additional functions for creating beautiful tables
    with 'gt'. The functions are generally wrappers around boilerplate or
    adding opinionated niche capabilities and helpers functions.
	"""
	
	homepage = "https://github.com/jthomasmock/gtExtras"
	cran = "gtExtras" 

	version("0.5.0", md5="4a0bd87d44aa8f7fe99f76d39059d76a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-gt@0.9:", type=("build", "run"))
	depends_on("r-commonmark", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-fontawesome@0.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-glue@1.6.1:", type=("build", "run"))
	depends_on("r-htmltools@0.5.3:", type=("build", "run"))
	depends_on("r-paletteer@1.4:", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-knitr@1.35:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
