# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaigespack(RPackage):
	"""Functions to handle cDNA microarray data, including several methods of data analysis

	This package uses functions of various other packages together with other functions in a coordinated way to handle and analyse cDNA microarray data
	"""
	
	homepage = "http://www.maiges.org/en/software/"
	bioc = "maigesPack" 

	version("1.66.0", commit="57de0bde155bc887c72533db42889c380ea6c8fa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-convert", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
