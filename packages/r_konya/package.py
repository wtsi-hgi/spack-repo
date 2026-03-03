# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKonya(RPackage):
	"""R Wrapper for Konya Municipality Open Data Portal

	Call the data wrappers for Konya Metropolitan Municipality's Open Data Portal <https://acikveri.konya.bel.tr/>. This will return all datasets stored in different formats. 
	"""
	
	homepage = "https://github.com/ozancanozdemir/bursa"
	cran = "konya" 

	version("0.1.0", md5="739f38da69c54d74f9b82f5fe1cf825f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
