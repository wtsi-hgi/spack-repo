# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasypackages(RPackage):
	"""Easy Loading and Installing of Packages

	Easily load and install multiple packages from different sources, 
    including CRAN and GitHub. The libraries function allows you to load or attach 
    multiple packages in the same function call. The packages function will load one 
    or more packages, and install any packages that are not installed on your system 
    (after prompting you). Also included is a from_import function that allows you 
    to import specific functions from a package into the global environment.
	"""
	
	cran = "easypackages" 

	version("0.1.0", md5="76ec5bda0e6b7c54b9b58d08522551f7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
