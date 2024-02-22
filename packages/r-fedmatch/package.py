# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFedmatch(RPackage):
	"""Fast, Flexible, and User-Friendly Record Linkage Methods

	Provides a flexible set of tools for matching two un-linked data sets. 
    'fedmatch' allows for three ways to match data: exact matches, fuzzy matches, and multi-variable matches. 
    It also allows an easy combination of these three matches via the tier matching function.
	"""
	
	cran = "fedmatch" 

	version("2.0.5", md5="666a09ecda73c70af4500503a3d68dfc")

	depends_on("r@3.5.3:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
