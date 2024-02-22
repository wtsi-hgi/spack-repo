# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBs4cards(RPackage):
	"""Generate Bootstrap Cards

	Allows the user to generate bootstrap cards within
    R markdown documents. Intended for use in conjunction with
    R markdown HTML outputs and other formats that support the 
    bootstrap 4 library.
	"""
	
	homepage = "https://github.com/djnavarro/bs4cards"
	cran = "bs4cards" 

	version("0.1.1", md5="8fd9d6750081c9fd96460015ee8d8be2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
