# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2dt(RPackage):
	"""Translation of Base R-Like Functions for 'data.table' Objects

	Some heavily used base R functions are reconstructed to also be compliant to data.table objects. Also, some general helper functions that could be of interest for working with data.table objects are included.
	"""
	
	cran = "R2DT" 

	version("0.2", md5="b8f6c5f8756ef8cd3998c053991a1454")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-devfunc", type=("build", "run"))
