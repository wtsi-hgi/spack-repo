# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBstrl(RPackage):
	"""Bayesian Streaming Record Linkage

	Perform record linkage on streaming files using recursive Bayesian updating.
	"""
	
	cran = "bstrl" 

	version("1.0.2", md5="2e2cce27b0648633aa81a96555bbff1b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-brl", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
