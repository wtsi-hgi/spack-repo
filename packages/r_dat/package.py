# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDat(RPackage):
	"""Tools for Data Manipulation

	An implementation of common higher order functions with syntactic
    sugar for anonymous function. Provides also a link to 'dplyr' and
    'data.table' for common transformations on data frames to work around non
    standard evaluation by default.
	"""
	
	cran = "dat" 

	version("0.5.0", md5="cf1b044c9bb8dfcd96d4efc261b1cade")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-aoos", type=("build", "run"))
