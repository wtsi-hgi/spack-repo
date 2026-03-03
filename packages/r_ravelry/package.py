# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRavelry(RPackage):
	"""An Interface to the 'Ravelry' API

	Provides access to the 'Ravelry' API <https://www.ravelry.com/groups/ravelry-api>. An R wrapper for pulling data from 'Ravelry.com', an organizational tool for crocheters, knitters, spinners, and weavers. You can retrieve pattern, yarn, author, and shop information by search or by a given id.  
	"""
	
	cran = "ravelRy" 

	version("0.1.0", md5="39e93276fd34a9fd83cb5db1777a7af4")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
