# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRglwidget(RPackage):
	"""'rgl' in 'htmlwidgets' Framework

	The contents of this package have
  been merged into rgl, so it is no longer needed.
	"""
	
	cran = "rglwidget" 

	version("0.2.1", md5="86823430333bc00a2841d3463e9ac069")

	depends_on("r-rgl@0.96:", type=("build", "run"))
