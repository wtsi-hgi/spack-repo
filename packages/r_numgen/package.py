# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNumgen(RPackage):
	"""Number Series Generator

	A number series generator that creates number series items based on cognitive models.
	"""
	
	cran = "numGen" 

	version("0.1.1", md5="5fca1e70d24e375c1b51d18e7aad02f4")

