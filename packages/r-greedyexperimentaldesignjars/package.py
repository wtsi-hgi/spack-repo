# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreedyexperimentaldesignjars(RPackage):
	"""GreedyExperimentalDesign JARs

	These are GreedyExperimentalDesign Java dependency libraries. Note: this package has no functionality of its own and should not be installed as a standalone package without GreedyExperimentalDesign.
	"""
	
	cran = "GreedyExperimentalDesignJARs" 

	version("1.0", md5="058d8de4467c0c23b4561d16cdf50dfa")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rjava@0.9.8:", type=("build", "run"))
	depends_on("openjdk@1.7:", type=("build", "link", "run"))
