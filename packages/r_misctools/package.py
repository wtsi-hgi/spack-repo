# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisctools(RPackage):
	"""Miscellaneous Tools and Utilities

	Miscellaneous small tools and utilities.
   Many of them facilitate the work with matrices,
   e.g. inserting rows or columns, creating symmetric matrices,
   or checking for semidefiniteness.
   Other tools facilitate the work with regression models,
   e.g. extracting the standard errors,
   obtaining the number of (estimated) parameters,
   or calculating R-squared values.
	"""
	
	homepage = "https://github.com/arne-henningsen/miscTools"
	cran = "miscTools" 

	version("0.6-28", md5="8e2c8d9b8bc2c021b6272556638506df")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
