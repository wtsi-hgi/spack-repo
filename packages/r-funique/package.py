# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunique(RPackage):
	"""A Faster Unique Function

	Similar to base's unique function, only optimized for working with 
    data frames, especially those that contain date-time columns.
	"""
	
	homepage = "https://github.com/mkearney/funique"
	cran = "funique" 

	version("0.0.1", md5="438a4c4f7bf045fe6e467ce2c493b196")

	depends_on("r@3.1:", type=("build", "run"))
