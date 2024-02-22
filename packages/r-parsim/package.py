# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParsim(RPackage):
	"""Parallel Simulation Studies

	Perform flexible simulation studies using one or multiple computer cores.
          The package is set up to be usable on high-performance clusters in addition
          to being run locally, see examples on <https://github.com/SachaEpskamp/parSim>.
	"""
	
	cran = "parSim" 

	version("0.1.5", md5="918fe068766fcf30c690ce14fc16f778")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
