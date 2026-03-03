# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilearray(RPackage):
	"""File-Backed Array for Out-of-Memory Computation

	Stores large arrays in files to avoid occupying large
    memories. Implemented with super fast gigabyte-level multi-threaded 
    reading/writing via 'OpenMP'. Supports multiple non-character data 
    types (double, float, complex, integer, logical, and raw).
	"""
	
	homepage = "https://dipterix.org/filearray/"
	cran = "filearray" 

	version("0.1.6", md5="b971a770de35e238d0ce74ed3ca09140")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fastmap@1.1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-uuid@1.1:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
