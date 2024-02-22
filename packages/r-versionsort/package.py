# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVersionsort(RPackage):
	"""Sort and Order Version Codes

	A lightweight package for sorting version codes in various forms. No strong dependencies guaranteed.
	"""
	
	cran = "versionsort" 

	version("1.1.0", md5="634bfff6a502f107a2cebbe19dbc839e")

