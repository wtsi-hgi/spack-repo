# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsagri(RPackage):
	"""Safety Assessment in Agricultural Field Trials

	Collection of functions, data sets and code examples 
 for evaluations of field trials with the objective of equivalence assessment.
	"""
	
	cran = "BSagri" 

	version("0.1-10", md5="a063c4d7ec3eae273483a9f6e8ef5eb6")

	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-mcpan", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mratios", type=("build", "run"))
