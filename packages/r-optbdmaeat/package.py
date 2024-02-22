# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptbdmaeat(RPackage):
	"""Optimal Block Designs for Two-Colour cDNA Microarray Experiments

	Computes A-, MV-, D- and E-optimal or near-optimal block designs for two-colour cDNA microarray experiments using the linear fixed effects and mixed effects models where the interest is in a comparison of all possible elementary treatment contrasts. The algorithms used in this package are based on the treatment exchange and array exchange algorithms of Debusho, Gemechu and Haines (2016, unpublished). The package also provides an optional method of using the graphical user interface (GUI) R package tcltk to ensure that it is user friendly.
	"""
	
	cran = "optbdmaeAT" 

	version("1.0.1", md5="f64812a8d46ff2842117f2c4bbfa0f29")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
