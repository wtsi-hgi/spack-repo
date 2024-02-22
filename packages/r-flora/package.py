# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlora(RPackage):
	"""Tools for Interacting with the Brazilian Flora 2020

	Tools to quickly compile taxonomic and distribution data from
    the Brazilian Flora 2020.
	"""
	
	homepage = "http://www.github.com/gustavobio/flora"
	cran = "flora" 

	version("0.3.4", md5="8f39bc52d28ead317a698f1252f60b26")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
