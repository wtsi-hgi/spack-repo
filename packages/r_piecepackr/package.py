# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPiecepackr(RPackage):
	"""Board Game Graphics

	Functions to make board game graphics with the 'ggplot2', 'grid', 'rayrender', 'rayvertex', and 'rgl' packages.  Specializes in game diagrams, animations, and "Print & Play" layouts for the 'piecepack' <https://www.ludism.org/ppwiki> but can make graphics for other board game systems.  Includes configurations for several public domain game systems such as checkers, (double-18) dominoes, go, 'piecepack', playing cards, etc.
	"""
	
	homepage = "https://trevorldavis.com/piecepackr/"
	cran = "piecepackr" 

	version("1.13.10", md5="9c35dde3b21b1ab5b38fa5ca04f5a7d1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gridgeometry", type=("build", "run"))
	depends_on("r-grimport2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
