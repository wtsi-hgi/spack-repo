# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXmlr(RPackage):
	"""Read, Write and Work with 'XML' Data

	'XML' package for creating and reading and manipulating 'XML', with an object model based on 'Reference Classes'.
	"""
	
	homepage = "https://github.com/Alipsa/xmlr"
	cran = "xmlr" 

	version("0.1.2", md5="73957a1e5a80cf9b127595d3bb54cafb")

	depends_on("r@3.1:", type=("build", "run"))
