# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBirk(RPackage):
	"""MA Birk's Functions

	Collection of tools to make R more convenient. Includes tools to
    summarize data using statistics not available with base R and manipulate
    objects for analyses.
	"""
	
	cran = "birk" 

	version("2.1.2", md5="ed20889a3e63164c12f2f5c689d34839")

