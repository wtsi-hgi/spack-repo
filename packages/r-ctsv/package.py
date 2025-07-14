# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtsv(RPackage):
	"""Identification of cell-type-specific spatially variable genes accounting for excess zeros

	The R package CTSV implements the CTSV approach developed by Jinge Yu and Xiangyu Luo that detects cell-type-specific spatially variable genes accounting for excess zeros. CTSV directly models sparse raw count data through a zero-inflated negative binomial regression model, incorporates cell-type proportions, and performs hypothesis testing based on R package pscl. The package outputs p-values and q-values for genes in each cell type, and CTSV is scalable to datasets with tens of thousands of genes measured on hundreds of spots. CTSV can be installed in Windows, Linux, and Mac OS.
	"""
	
	homepage = "https://github.com/jingeyu/CTSV"
	bioc = "CTSV"

	version("1.10.0", commit="5b5092c8ef63aa3fee82cc12d9f838be9a43440f")
	version("1.4.0", commit="c5da80cf8a3397d1978d3552a03caaa3730d4f7a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
