# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCctutorial(RPackage):
	"""Data package for ChIP-chip tutorial

	This is a data package that accompanies a ChIP-chip tutorial, which has been published in PLoS Computational Biology. The data and source code in this package allow the reader to completely reproduce the steps in the tutorial.
	"""
	
	bioc = "ccTutorial"

	version("1.40.0", commit="6feba2b5b8bc09ed156d90c8724a715520a75d13")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ringo@1.9.8:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-topgo@1.13.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

