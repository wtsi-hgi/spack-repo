# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElt(RPackage):
	"""Experience Life Tables

	Build experience life tables.
	"""
	
	cran = "ELT" 

	version("1.7", md5="831f929a338ed24d83a1f429b2963b57")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
