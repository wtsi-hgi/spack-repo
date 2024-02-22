# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfiniumpurify(RPackage):
	"""Estimate and Account for Tumor Purity in Cancer Methylation Data
Analysis

	The proportion of cancer cells in solid tumor sample, known as the tumor purity, has adverse impact on a variety of data analyses if not properly accounted for. We develop 'InfiniumPurify', which is a comprehensive R package for estimating and accounting for tumor purity based on DNA methylation Infinium 450k array data. 'InfiniumPurify' provides functionalities for tumor purity estimation. In addition, it can perform differential methylation detection and tumor sample clustering with the consideration of tumor purities. 
	"""
	
	cran = "InfiniumPurify" 

	version("1.3.1", md5="c10ffaab88f95fd1e10f02a72bb30fbf")

	depends_on("r-matrixstats", type=("build", "run"))
