# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnsvg(RPackage):
	"""Scalable identification of spatially variable genes in spatially-resolved transcriptomics data

	Method for scalable identification of spatially variable genes (SVGs) in spatially-resolved transcriptomics data. The method is based on nearest-neighbor Gaussian processes and uses the BRISC algorithm for model fitting and parameter estimation. Allows identification and ranking of SVGs with flexible length scales across a tissue slide or within spatial domains defined by covariates. Scales linearly with the number of spatial locations and can be applied to datasets containing thousands or more spatial locations.
	"""
	
	homepage = "https://github.com/lmweber/nnSVG"
	bioc = "nnSVG"

	version("1.12.0", commit="b308132eccfe7ecd832cd2a0483dc11f19aaa67c")
	version("1.6.4", commit="f68dffb34cc425b2e67730468523b7076247be2e")
	version("1.6.0", md5="4af169b12d944eff8ee9d9e3063ff5ea")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-brisc", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
