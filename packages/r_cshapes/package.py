# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCshapes(RPackage):
	"""The CShapes 2.0 Dataset and Utilities

	Package for CShapes 2.0, a GIS dataset of country borders (1886-today). Includes functions for data extraction and the computation of distance matrices and -lists.
	"""
	
	cran = "cshapes" 

	version("2.0", md5="e28dc4f2285349245dde78a5347b30c2")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rmapshaper", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
