# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtilsipea(RPackage):
	"""IPEA Common Functions

	The most used functions on IPEA (Instituto de Pesquisa Economica Aplicada). 
             Most of functions deal with brazilian names. 
             It can guess the women single's name, extract prepositions or extract the first name.
	"""
	
	homepage = "https://github.com/ipea/utilsIPEA"
	cran = "utilsIPEA" 

	version("0.0.6", md5="eb531ae7f20c769e46f85d8ec63d4084")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
