# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrajectories(RPackage):
	"""Classes and Methods for Trajectory Data

	Classes and methods for trajectory data, with support for nesting individual Track objects in track sets (Tracks) and track sets for different entities in collections of Tracks. Methods include selection, generalization, aggregation, intersection, simulation, and plotting.
	"""
	
	homepage = "https://github.com/edzer/trajectories"
	cran = "trajectories" 

	version("0.2-8", md5="a434ed1a94c0a87e3c579f487d227cf6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-sp@1.1.0:", type=("build", "run"))
	depends_on("r-spacetime@1.0.0:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
