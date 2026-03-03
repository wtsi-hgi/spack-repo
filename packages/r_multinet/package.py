# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultinet(RPackage):
	"""Analysis and mining of multilayer social networks

	Functions for the creation/generation and analysis of multilayer social networks <doi:10.18637/jss.v098.i08>.
	"""
	
	cran = "multinet" 

	version("4.1.2", md5="5892279760ef094b883cb0195c24614b")

	depends_on("r-igraph@1.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
