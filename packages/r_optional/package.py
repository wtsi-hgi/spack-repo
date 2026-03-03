# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptional(RPackage):
	"""Optional Types and Pattern Matching

	Introduces optional types with some() and none, as well as match_with() from functional languages.
	"""
	
	cran = "optional" 

	version("2.0.1", md5="416c32e087cf69025892b6ce7fd02674")

	depends_on("r-magrittr", type=("build", "run"))
