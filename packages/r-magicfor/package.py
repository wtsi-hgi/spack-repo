# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagicfor(RPackage):
	"""Magic Functions to Obtain Results from for Loops

	Magic functions to obtain results from for loops.
	"""
	
	homepage = "https://github.com/hoxo-m/magicfor"
	cran = "magicfor" 

	version("0.1.0", md5="ae8dea81cc74140dca9d0d30c2af016a")

