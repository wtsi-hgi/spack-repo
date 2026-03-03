# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPluscode(RPackage):
	"""Encoder for Google 'Pluscodes'

	Retrieves a 'pluscode' by inputting latitude and longitude. Includes additional functions to retrieve neighbouring 'pluscodes'.
	"""
	
	cran = "pluscode" 

	version("0.1.0", md5="7d7dd2c7d248fe55c1303932935b2042")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
