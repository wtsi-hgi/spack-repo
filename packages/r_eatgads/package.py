# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REatgads(RPackage):
	"""Data Management of Large Hierarchical Data

	Import 'SPSS' data, handle and change 'SPSS' meta data, store and access large hierarchical data in 'SQLite' data bases.
	"""
	
	homepage = "https://github.com/beckerbenj/eatGADS"
	cran = "eatGADS" 

	version("1.1.0", md5="1800a4903aecaca89d15083c86199826")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-eatdb@0.5:", type=("build", "run"))
	depends_on("r-haven@2.4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-eattools@0.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
