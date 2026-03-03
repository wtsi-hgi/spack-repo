# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSapp(RPackage):
	"""Statistical Analysis of Point Processes

	Functions for statistical analysis of point processes.
	"""
	
	cran = "SAPP" 

	version("1.0.9-1", md5="b5c7d0e5d62fb0db414e014afe192b03")

	depends_on("r@4:", type=("build", "run"))
