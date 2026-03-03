# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViafr(RPackage):
	"""Interface to the 'VIAF' ('Virtual International Authority File')
API

	Provides direct access to linked names for the same entity across the world's major name authority files, including national and regional variations in language, character set, and spelling. For more information go to <https://viaf.org/>.
	"""
	
	homepage = "https://github.com/stefanieschneider/viafr"
	cran = "viafr" 

	version("0.3.0", md5="ad060f2bfb5cd9c92dc0c0cd7a740353")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-utf8", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
