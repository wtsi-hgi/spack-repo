# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexposition(RPackage):
	"""Two-Table ExPosition

	An extension of ExPosition for two table analyses, specifically, discriminant analyses.
	"""
	
	cran = "TExPosition" 

	version("2.6.10.1", md5="04179cffd16611750fbfe62df6d64346")

	depends_on("r-prettygraphs@2.1.4:", type=("build", "run"))
	depends_on("r-exposition@2:", type=("build", "run"))
