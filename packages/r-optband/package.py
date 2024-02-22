# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptband(RPackage):
	"""'surv' Object Confidence Bands Optimized by Area

	Given a certain coverage level, obtains simultaneous confidence
    bands for the survival and cumulative hazard functions such that the area
    between is minimized. Produces an approximate solution based on local time
    arguments.
	"""
	
	homepage = "https://github.com/seasamgo/optband"
	cran = "optband" 

	version("0.2.2", md5="8d104dade31af753f1968d394c475075")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lambertw", type=("build", "run"))
