# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmut(RPackage):
	"""Multi-SNP Mediation Intersection-Union Test

	Testing the mediation effect of multiple SNPs on an outcome through a mediator.
	"""
	
	cran = "SMUT" 

	version("1.1", md5="926924725387fc82fabb5570af6e45ba")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-skat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
