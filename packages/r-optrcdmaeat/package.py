# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptrcdmaeat(RPackage):
	"""Optimal Row-Column Designs for Two-Colour cDNA Microarray
Experiments

	Computes A-, MV-, D- and E-optimal or near-optimal row-column designs for two-colour cDNA microarray experiments using the linear fixed effects and mixed effects models where the interest is in a comparison of all pairwise treatment contrasts. The algorithms used in this package are based on the array exchange and treatment exchange algorithms adopted from Debusho, Gemechu and Haines (2016, unpublished) algorithms after adjusting for the row-column designs setup. The package also provides an optional method of using the graphical user interface (GUI) R package tcltk to ensure that it is user friendly.
	"""
	
	cran = "optrcdmaeAT" 

	version("1.0.0", md5="0d464431bce6d1de1d5eb336bacf09a1")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
