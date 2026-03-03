# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFstpackage(RPackage):
	"""Unified Sequence-Based Association Tests Allowing for Multiple
Functional Annotation Scores

	Functions for sequencing studies allowing for multiple functional annotation scores. Score type tests and an efficient perturbation method are used for individual gene/large gene-set/genome wide analysis. Only summary statistics are needed.
	"""
	
	cran = "FSTpackage" 

	version("0.1", md5="c47c93d65241b92c028fe5290f1e3e11")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-skat", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
