# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcookbook(RPackage):
	"""Data for "R Graphics Cookbook"

	Data sets used in the book "R Graphics Cookbook" by Winston
    Chang, published by O'Reilly Media.
	"""
	
	cran = "gcookbook" 

	version("2.0", md5="a2a17506ce112d0c81555cac7ac1d81f")

	depends_on("r@2.10:", type=("build", "run"))
