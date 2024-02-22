# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqdatatable(RPackage):
	"""'rquery' for 'data.table'

	Implements the 'rquery' piped Codd-style query algebra using 'data.table'.  This allows
   for a high-speed in memory implementation of Codd-style data manipulation tools.
	"""
	
	homepage = "https://github.com/WinVector/rqdatatable/"
	cran = "rqdatatable" 

	version("1.3.3", md5="a1af5f6a26c66051cc445631a5c173ea")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-wrapr@2.0.9:", type=("build", "run"))
	depends_on("r-rquery@1.4.9:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
