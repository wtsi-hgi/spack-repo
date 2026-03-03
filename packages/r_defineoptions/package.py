# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDefineoptions(RPackage):
	"""Define and Parse Command Line Options

	Parses command line arguments and supplies values to scripts. Users can specify names to which parsed inputs are assigned, value types into which inputs are cast, long options or short options, input splitters and callbacks that define how options should be specified and how input values are supplied.
	"""
	
	homepage = "https://github.com/niceume/defineOptions"
	cran = "defineOptions" 

	version("0.9", md5="025f1e568640e38972b47d69b44f9314")

