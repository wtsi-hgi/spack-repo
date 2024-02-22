# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeprechaun(RPackage):
	"""Create Simple 'Shiny' Applications as Packages

	Code generator for robust dependency-free 'Shiny' 
    applications in the form of packages. It includes numerous
    convenience functions to create modules, include utility 
    functions to create common 'Bootstrap' elements, setup a
    project from the ground-up, and much more.
	"""
	
	cran = "leprechaun" 

	version("1.0.0", md5="5967a9d88219638d022029eb88a4fcc1")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
