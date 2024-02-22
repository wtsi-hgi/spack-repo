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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CTSV_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CTSV/CTSV_1.4.0.tar.gz"]

	version("1.4.0", md5="4a3f8c7b5398449ea01b312ed7da1f43")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
