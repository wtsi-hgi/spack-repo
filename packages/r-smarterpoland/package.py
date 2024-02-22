# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmarterpoland(RPackage):
	"""Tools for Accessing Various Datasets Developed by the Foundation
SmarterPoland.pl

	Tools for accessing and processing datasets prepared by the Foundation SmarterPoland.pl. Among all: access to API of Google Maps, Central Statistical Office of Poland, MojePanstwo, Eurostat, WHO and other sources.
	"""
	
	cran = "SmarterPoland" 

	version("1.8.1", md5="d1855d354488d98892398dfb4b32a0e8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
