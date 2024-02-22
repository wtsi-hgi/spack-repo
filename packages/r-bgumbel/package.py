# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgumbel(RPackage):
	"""Bimodal Gumbel Distribution

	Bimodal Gumbel distribution. General functions for performing extreme value analysis.
	"""
	
	homepage = "https://CRAN.R-project.org/package=bgumbel"
	cran = "bgumbel" 

	version("0.0.3", md5="e6005dd78b2aad8b8371825b618673bb")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
