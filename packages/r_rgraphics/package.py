# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgraphics(RPackage):
	"""Data and Functions from the Book R Graphics, Third Edition

	Data and Functions from the book R Graphics, Third Edition. There is a function to produce each figure in the book, plus several functions, classes, and methods defined in Chapter 8.  
	"""
	
	homepage = "https://www.stat.auckland.ac.nz/~paul/RG3e/index.html"
	cran = "RGraphics" 

	version("3.0-2", md5="233d851a2dfb10d07b3cd47d70b9af1c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-grimport", type=("build", "run"))
	depends_on("r-grimport2", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-gridgraphics", type=("build", "run"))
	depends_on("r-gridsvg", type=("build", "run"))
