# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrapes(RPackage):
	"""Make Binary Operators

	Turn arbitrary functions into binary operators.
	"""
	
	homepage = "https://github.com/wlandau/grapes"
	cran = "grapes" 

	version("1.0.0", md5="4758f9ae74879a7fffb7ae5cc52296c3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
