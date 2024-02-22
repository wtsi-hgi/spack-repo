# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGo2bigq(RPackage):
	"""Convert Large Numbers to Bigq Format

	This function converts mfpr, numeric, or character strings representing numbers to bigq format without loss of precision. 
	"""
	
	cran = "go2bigq" 

	version("2.0.1", md5="edb3391266b2f2435d44d0cdaedf1929")

	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
