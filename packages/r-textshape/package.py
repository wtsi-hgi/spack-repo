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

	version("1.7.5", md5="b92a38c5024eed8bf087992fa3465795")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
