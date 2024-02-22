# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebus(RPackage):
	"""Build Regular Expressions in a Human Readable Way

	Build regular expressions piece by piece using human readable code.
    This package is designed for interactive use.  For package development, use
    the rebus.* dependencies.
	"""
	
	cran = "rebus" 

	version("0.1-3", md5="8c9981f559c3eb3e7e489177958f49bb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rebus-base@0.0.3:", type=("build", "run"))
	depends_on("r-rebus-datetimes", type=("build", "run"))
	depends_on("r-rebus-numbers", type=("build", "run"))
	depends_on("r-rebus-unicode@0.0.2:", type=("build", "run"))
