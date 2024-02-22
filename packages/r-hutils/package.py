# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHutils(RPackage):
	"""Miscellaneous R Functions and Aliases

	Provides utility functions for, and drawing on, the 'data.table' package. The package also collates useful miscellaneous functions extending base R not available elsewhere. The name is a portmanteau of 'utils' and the author.
	"""
	
	homepage = "https://github.com/hughparsonage/hutils"
	cran = "hutils" 

	version("1.8.1", md5="80ea32a2bf6ecc7ae5ef281253f2b7cd")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
