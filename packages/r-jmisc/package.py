# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmisc(RPackage):
	"""Julian Miscellaneous Function

	Some handy function in R.
	"""
	
	cran = "Jmisc" 

	version("0.3.1.1", md5="1aa2893d1477bb0cae910a0ae527728f")

