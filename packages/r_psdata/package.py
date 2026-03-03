# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsdata(RPackage):
	"""Download Regularly Maintained Political Science Data Sets

	This R package includes functions for gathering commonly used and
    regularly maintained data set in political science. It also includes
    functions for combining components from these data sets into variables that
    have been suggested in the literature, but are not regularly maintained.
	"""
	
	homepage = "http://cran.r-project.org/package=psData"
	cran = "psData" 

	version("0.2.2", md5="9849707cdcbf82b1eedbc20731a8cea5")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-datacombine", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
