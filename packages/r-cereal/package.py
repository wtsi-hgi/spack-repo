# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCereal(RPackage):
	"""Serialize 'vctrs' Objects to 'JSON'

	The 'vctrs' package provides a concept of vector prototype
    that can be especially useful when deploying models and code.  Serialize 
    these object prototypes to 'JSON' so they can be used to check and coerce 
    data in production systems, and deserialize 'JSON' back to the correct 
    object prototypes.
	"""
	
	homepage = "https://r-lib.github.io/cereal/"
	cran = "cereal" 

	version("0.1.0", md5="0b092b7f43d0bce5d7ff599accb229c4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
