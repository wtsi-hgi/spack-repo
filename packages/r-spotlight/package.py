# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpotlight(RPackage):
	"""`SPOTlight`: Spatial Transcriptomics Deconvolution

	`SPOTlight`provides a method to deconvolute spatial transcriptomics spots using a seeded NMF approach along with visualization tools to assess the results. Spatially resolved gene expression profiles are key to understand tissue organization and function. However, novel spatial transcriptomics (ST) profiling techniques lack single-cell resolution and require a combination with single-cell RNA sequencing (scRNA-seq) information to deconvolute the spatially indexed datasets. Leveraging the strengths of both data types, we developed SPOTlight, a computational tool that enables the integration of ST with scRNA-seq data to infer the location of cell types and states within a complex tissue. SPOTlight is centered around a seeded non-negative matrix factorization (NMF) regression, initialized using cell-type marker genes and non-negative least squares (NNLS) to subsequently deconvolute ST capture locations (spots).
	"""
	
	homepage = "https://github.com/MarcElosua/SPOTlight"
	bioc = "SPOTlight"

	version("1.12.1", commit="55527f637c6921fad907f3a6b2a02946efaa16d9")
	version("1.6.7", commit="e9de3a67218ffd7909f1c6c6f443fc9af106af7e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-sparsematrixstats", type=("build", "run"))
