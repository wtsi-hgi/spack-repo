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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CTSV_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CTSV/CTSV_1.4.0.tar.gz"]

    version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="c9ab303473fa093de52c3a25dc2e46413399cef5284aa2c177299c03e61fcc02")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
