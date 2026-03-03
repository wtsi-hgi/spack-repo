# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROx(RPackage):
	"""Shorthand if-Else

	Short hand if-else function to easily switch the values depending
  on a logical condition.
	"""
	
	cran = "ox" 

	version("0.1.0", md5="8c771e9a50bea25f5ab8b962450d4fbf")

	depends_on("r@3:", type=("build", "run"))
