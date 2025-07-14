# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpgsea(RPackage):
	"""Permutation approximation methods for gene set enrichment analysis (non-permutation GSEA)

	Current gene set enrichment methods rely upon permutations for inference.  These approaches are computationally expensive and have minimum achievable p-values based on the number of permutations, not on the actual observed statistics.  We have derived three parametric approximations to the permutation distributions of two gene set enrichment test statistics.  We are able to reduce the computational burden and granularity issues of permutation testing with our method, which is implemented in this package. npGSEA calculates gene set enrichment statistics and p-values without the computational cost of permutations.  It is applicable in settings where one or many gene sets are of interest.  There are also built-in plotting functions to help users visualize results.
	"""
	
	bioc = "npGSEA"

	version("1.44.0", commit="a5240a3e6cc058c439cf4f11816b47a0152f5c6b")
	version("1.38.0", commit="315781391ef321f44bbcd24075a94b94a6aa44df")

	depends_on("r-gseabase@1.24:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
