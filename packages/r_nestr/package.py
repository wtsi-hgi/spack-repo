# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestr(RPackage):
	"""Build Nesting or Hierarchical Structures

	Facilitates building a nesting or hierarchical structure as a list or data frame by using a human friendly syntax. 
	"""
	
	cran = "nestr" 

	version("0.1.2", md5="7326bf5e85d9cccfb5a981cb4799fa62")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
