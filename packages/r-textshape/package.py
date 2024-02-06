# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextshape(RPackage):
	"""Tools for Reshaping Text

	Tools that can be used to reshape and restructure text data.
	"""
	
	homepage = "https://github.com/trinker/textshape"
	cran = "textshape" 

	version("1.7.3", md5="4ba7cedca6530e84803f2d1e6a4a7b1e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
