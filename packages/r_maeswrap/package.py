# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaeswrap(RPackage):
	"""Wrapper Functions for MAESTRA/MAESPA

	A bundle of functions for modifying MAESTRA/MAESPA input files,reading output files, and visualizing the stand in 3D. Handy for running sensitivity analyses, scenario analyses, etc.
	"""
	
	cran = "Maeswrap" 

	version("1.7", md5="4312bfeb495bf34dada1754e0370be0f")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
