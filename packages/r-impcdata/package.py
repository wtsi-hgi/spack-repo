# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpcdata(RPackage):
	"""Retrieves data from IMPC database

	Package contains methods for data retrieval from IMPC Database.
	"""
	
	bioc = "IMPCdata"

	version("1.44.0", commit="fd8c39d0876630d187429341469cb6771c00df8f")
	version("1.38.0", commit="8fa0d84f3c9a534427eb952c48e19e331a83039b")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
