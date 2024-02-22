# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVwline(RPackage):
	"""Draw Variable-Width Lines

	Provides R functions to draw lines and curves with the width
             of the curve allowed to vary along the length of the curve.
	"""
	
	homepage = "https://github.com/pmur002/vwline"
	cran = "vwline" 

	version("0.2-2", md5="06a47cbca4bb0a62aaee33749b6ceb68")

	depends_on("r-polyclip", type=("build", "run"))
	depends_on("r-gridbezier", type=("build", "run"))
