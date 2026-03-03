# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCepp(RPackage):
	"""Context Driven Exploratory Projection Pursuit

	Functions and Data to support Context Driven Exploratory Projection Pursuit.
	"""
	
	cran = "cepp" 

	version("1.7", md5="d78c591e426185a13174051984c3352e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
