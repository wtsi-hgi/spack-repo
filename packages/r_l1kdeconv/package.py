# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL1kdeconv(RPackage):
	"""Deconvolution for LINCS L1000 Data

	LINCS L1000 is a high-throughput technology that allows the gene expression measurement in a large number of assays. However, to fit the measurements of ~1000 genes in the ~500 color channels of LINCS L1000, every two landmark genes are designed to share a single channel. Thus, a deconvolution step is required to infer the expression values of each gene. Any errors in this step can be propagated adversely to the downstream analyses. We present a LINCS L1000 data peak calling R package l1kdeconv based on a new outlier detection method and an aggregate Gaussian mixture model. Upon the remove of outliers and the borrowing information among similar samples, l1kdeconv shows more stable and better performance than methods commonly used in LINCS L1000 data deconvolution.
	"""
	
	cran = "l1kdeconv" 

	version("1.2.0", md5="bed88ccece7e666e20353041ffb4f00f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
