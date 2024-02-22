# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmr(RPackage):
	"""Matrix Multiplication on Data.frames

	Simple helpers for matrix multiplication on data.frames. These allow for more
    concise code during low level mathematical operations, and help ensure code is more
    easily read, understood, and serviced. 
	"""
	
	homepage = "https://github.com/stevecondylios/mmr"
	cran = "mmr" 

	version("0.1.0", md5="e570e36866ce9cbb1816d582e3f5777b")

