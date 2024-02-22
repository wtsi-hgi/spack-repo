# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfix(RPackage):
	"""Basic Infix Binary Operators

	Contains a number of infix binary operators that may be useful in day to day practices.
	"""
	
	homepage = "http://github.com/ebeneditos/infix"
	cran = "infix" 

	version("0.1.0", md5="4a95122f3bfbcf463965d220e0b78528")

	depends_on("r-magrittr", type=("build", "run"))
