# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REply(RPackage):
	"""Apply a Function Over Expressions

	Evaluate a function over a data frame of expressions.
	"""
	
	homepage = "https://github.com/wlandau/eply"
	cran = "eply" 

	version("0.1.2", md5="208b6070dce374ea4bf176f5e8e661fc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
