# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValet(RPackage):
	"""Provide R Client to the Bank of Canada's Valet API

	The Bank of Canada updated their Valet API
             <https://www.bankofcanada.ca/valet/docs>, and no R client
             currently exists. This provides access to all of Valet's endpoints
             and serves responses in wide format easy for researchers to
             handle but also provides tools to access API responses as a list.
	"""
	
	homepage = "runkelcorey.github.io/valet"
	cran = "valet" 

	version("0.9.0", md5="c7738d0973dafbb691ec3d22d1e0fec8")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
