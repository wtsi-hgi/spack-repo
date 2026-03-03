# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiconvr(RPackage):
	"""Fetch Data from Plataforma +Brasil (SICONV)

	Fetch data on targeted public investments from Plataforma +Brasil (SICONV) <http://plataformamaisbrasil.gov.br/>, 
    the responsible system for requests, execution, and monitoring of federal discretionary transfers in Brazil.
	"""
	
	homepage = "https://github.com/meirelesff/siconvr"
	cran = "siconvr" 

	version("0.0.1", md5="258de1bd40d493cc5d4a886c89e1bf93")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
