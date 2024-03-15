# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRd2roxygen(RPackage):
	"""Convert Rd to 'Roxygen' Documentation

	Functions to convert Rd to 'roxygen' documentation. It can parse an
    Rd file to a list, create the 'roxygen' documentation and update the original
    R script (e.g. the one containing the definition of the function)
    accordingly. This package also provides utilities that can help developers
    build packages using 'roxygen' more easily. The 'formatR' package can be used
    to reformat the R code in the examples sections so that the code will be
    more readable.
	"""
	
	homepage = "https://github.com/yihui/Rd2roxygen"
	cran = "Rd2roxygen" 

	version("1.15", md5="e909ffd31191146310d708f6b9f982ea")

	depends_on("r-roxygen2@4:", type=("build", "run"))
	depends_on("r-xfun@0.13:", type=("build", "run"))
	depends_on("r-formatr@1:", type=("build", "run"))
