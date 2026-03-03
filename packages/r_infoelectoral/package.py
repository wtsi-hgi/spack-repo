# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfoelectoral(RPackage):
	"""Download Spanish Election Results

	Download official election results for Spain at polling station, municipality and province level from the Ministry of Interior (<https://infoelectoral.interior.gob.es/es/elecciones-celebradas/area-de-descargas/>), format them and import them to the R environment.
	"""
	
	homepage = "https://github.com/rOpenSpain/infoelectoral"
	cran = "infoelectoral" 

	version("1.0.0", md5="173a069b83b5c9fad0993b02d333b62d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
