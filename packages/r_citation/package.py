# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitation(RPackage):
	"""Software Citation Tools

	A collection of functions to extract citation information from 'R' packages and to deal with files in 'citation file format' (<https://citation-file-format.github.io/>), extending the functionality already provided by the citation() function in the 'utils' package.
	"""
	
	homepage = "https://github.com/pik-piam/citation"
	cran = "citation" 

	version("0.8.2", md5="e2e763939c7034c5fe5207fe113575d1")

	depends_on("r-desc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
