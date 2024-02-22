# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadit(RPackage):
	"""Effortlessly Read Any Rectangular Data

	
    Providing just one primary function, 'readit' uses a set of reasonable
    heuristics to apply the appropriate reader function to the given file path.
    As long as the data file has an extension, and the data is (or can be
    coerced to be) rectangular, readit() can probably read it.
	"""
	
	homepage = "https://github.com/ryapric/readit"
	cran = "readit" 

	version("1.0.0", md5="1ef4cf0d133f8aaf1e14e2d9557ca515")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-haven@1.1.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-readxl@1:", type=("build", "run"))
