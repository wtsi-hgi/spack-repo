# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2r(RPackage):
	"""R-Object to R-Object Hash Maps

	
	Implementation of hash tables (hash sets and hash maps) in R, 
	featuring arbitrary R objects as keys, 
	arbitrary hash and key-comparison functions, 
	and customizable behaviour upon queries of missing keys.
	"""
	
	homepage = "https://github.com/vgherard/r2r"
	cran = "r2r" 

	version("0.1.1", md5="1e12fbba0965a7ba1204429de9f9c0b0")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
