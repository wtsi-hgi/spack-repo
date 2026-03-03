# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiverbuilder(RPackage):
	"""River Generation for Given Data Sets

	Generates graphs, CSV files, and coordinates related to river valleys when calling the riverbuilder() function.
	"""
	
	cran = "RiverBuilder" 

	version("0.1.1", md5="5eed05f210fd81f51717806213094a0a")

