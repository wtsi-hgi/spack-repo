# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHotspots(RPackage):
	"""Hot Spots

	The hotspots package is designed to look within a set of measured values of a variable and identify values that are disproportionately high based on both the deviance of any given value from a statistical distribution and its similarity to other values. Because this relative magnitude of each value is taken into account, a value that is a statistical outlier may not always be a hot spot if other values are similarly large.
	"""
	
	cran = "hotspots" 

	version("1.0.3", md5="41eab5d9638bcda6c0a37765d5b92c49")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
