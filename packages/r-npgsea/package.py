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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/npGSEA_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/npGSEA/npGSEA_1.38.0.tar.gz"]

	version("1.38.0", sha256="bcfdc31d99c7901b359ddc578764bbb987c6977aac1806d38dda95ef10a0a354")

	depends_on("r-gseabase@1.24:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
