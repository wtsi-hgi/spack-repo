# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpurs(RPackage):
	"""Functions and Datasets for "Introduction to Scientific
Programming and Simulation Using R"

	Provides functions and datasets from Jones, O.D., R. Maillardet, and A.P. Robinson.  2014.  An Introduction to Scientific Programming and Simulation, Using R. 2nd Ed. Chapman And Hall/CRC.
	"""
	
	cran = "spuRs" 

	version("2.0.2", md5="d1b6c649637a5cf312dd1252dd0bdcbd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
