# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfast(RPackage):
	"""Probabilistic Factor Analysis for Spatially-Aware Dimension
Reduction

	Probabilistic factor analysis for spatially-aware dimension reduction across multi-section spatial transcriptomics data with millions of spatial locations.
    More details can be referred to Wei Liu, et al. (2023) <doi:10.1101/2023.07.11.548486>.
	"""
	
	homepage = "https://github.com/feiyoung/ProFAST"
	cran = "ProFAST" 

	version("1.3", md5="4ad4e6a81986d5820d12ecbfb57f6286")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dr-sc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-precast", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
	depends_on("r-harmony", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
