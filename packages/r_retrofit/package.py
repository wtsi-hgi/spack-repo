# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRetrofit(RPackage):
	"""RETROFIT: Reference-free deconvolution of cell mixtures in spatial transcriptomics

	RETROFIT is a Bayesian non-negative matrix factorization framework to decompose cell type mixtures in ST data without using external single-cell expression references. RETROFIT outperforms existing reference-based methods in estimating cell type proportions and reconstructing gene expressions in simulations with varying spot size and sample heterogeneity, irrespective of the quality or availability of the single-cell reference. RETROFIT recapitulates known cell-type localization patterns in a Slide-seq dataset of mouse cerebellum without using any single-cell data.
	"""
	
	homepage = "https://github.com/qunhualilab/retrofit"
	bioc = "retrofit" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/retrofit_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/retrofit/retrofit_1.2.0.tar.gz"]

	version("1.2.0", md5="2b804a752a293f14495e94adb39df466")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
