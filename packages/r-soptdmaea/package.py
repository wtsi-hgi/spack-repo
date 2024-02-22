# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoptdmaea(RPackage):
	"""Sequential Optimal Designs for Two-Colour cDNA Microarray
Experiments

	Computes sequential A-, MV-, D- and E-optimal or near-optimal block and row-column designs for two-colour cDNA microarray experiments using the linear fixed effects and mixed effects models where the interest is in a comparison of all possible elementary treatment contrasts. The package also provides an optional method of using the graphical user interface (GUI) R package 'tcltk' to ensure that it is user friendly.
	"""
	
	cran = "soptdmaeA" 

	version("1.0.0", md5="cd8936a6b05cc38877ca06245c452d28")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
