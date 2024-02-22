# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFail(RPackage):
	"""File Abstraction Interface Layer (FAIL)

	More comfortable interface to work with R data or source files
    in a key-value fashion.
	"""
	
	homepage = "https://github.com/mllg/fail"
	cran = "fail" 

	version("1.3", md5="45c4fd7a09f8db0715554b60f74c6120")

	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
