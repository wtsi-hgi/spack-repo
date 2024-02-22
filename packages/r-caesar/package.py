# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaesar(RPackage):
	"""Encrypts and Decrypts Strings

	Encrypts and decrypts strings using either the Caesar cipher or a
    pseudorandom number generation (using set.seed()) method.
	"""
	
	homepage = "https://github.com/jacobkap/caesar"
	cran = "caesar" 

	version("1.1.0", md5="eeec6f74df38921b6e430ba4677a92a1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-binhf", type=("build", "run"))
