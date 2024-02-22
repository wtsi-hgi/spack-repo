# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClsiep15(RPackage):
	"""Clinical and Laboratory Standards Institute (CLSI) EP15-A3
Calculations

	Calculations of "EP15-A3 document. A manual for user verification of precision and estimation of bias" CLSI (2014, ISBN:1-56238-966-1).
	"""
	
	cran = "CLSIEP15" 

	version("0.1.0", md5="840962f28136c11a0a6aadd12fe4ce3f", url="https://cran.r-project.org/src/contrib/CLSIEP15_0.1.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
