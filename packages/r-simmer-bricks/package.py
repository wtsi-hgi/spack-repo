# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimmerBricks(RPackage):
	"""Helper Methods for 'simmer' Trajectories

	Provides wrappers for common activity patterns in 'simmer' trajectories.
	"""
	
	homepage = "https://r-simmer.org"
	cran = "simmer.bricks" 

	version("0.2.2", md5="c2a771b8a48e241999515bdc976096cd")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-simmer@3.7:", type=("build", "run"))
