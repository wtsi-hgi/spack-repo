# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterd(RPackage):
	"""The Integrated and Robust Deconvolution

	We developed the Integrated and Robust Deconvolution algorithm to infer cell-type proportions from target bulk RNA-seq data. This package is able to effectively integrate deconvolution results from multiple scRNA-seq datasets and calibrates estimates from reference-based deconvolution by taking into account extra biological information as priors. Moreover, the proposed algorithm is robust to inaccurate external information imposed in the deconvolution system.
	"""
	
	homepage = "https://github.com/chencxxy28/InteRD"
	cran = "InteRD" 

	version("0.1.1", md5="a20190b1a270f2419aa0549e4a721a13")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
