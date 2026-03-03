# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdgebundle(RPackage):
	"""Algorithms for Bundling Edges in Networks and Visualizing Flow
and Metro Maps

	Implements several algorithms for bundling edges in networks and flow and metro map layouts. This includes force directed edge bundling <doi:10.1111/j.1467-8659.2009.01450.x>, a flow algorithm based on Steiner trees<doi:10.1080/15230406.2018.1437359> and a multicriteria optimization method for metro map layouts <doi:10.1109/TVCG.2010.24>.
	"""
	
	homepage = "https://github.com/schochastics/edgebundle"
	cran = "edgebundle" 

	version("0.4.2", md5="8bb5126adb90a1c04c2bb2a31ebd9bc5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
