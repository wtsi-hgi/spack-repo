# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScquantum(RPackage):
	"""Estimate Ploidy and Absolute Copy Number from Single Cell
Sequencing

	Given bincount data from single-cell copy number profiling (segmented or unsegmented), estimates ploidy, and uses the ploidy estimate to scale the data to absolute copy numbers. Uses the modular quantogram proposed by Kendall (1986) <doi:10.1002/0471667196.ess2129.pub2>, modified by weighting segments according to confidence, and quantifying confidence in the estimate using a theoretical quantogram. Includes optional fused-lasso segmentation with the algorithm in Johnson (2013) <doi:10.1080/10618600.2012.681238>, using the implementation from glmgen by Arnold, Sadhanala, and Tibshirani.
	"""
	
	cran = "scquantum" 

	version("1.0.0", md5="429250ddcf4efe0537d2542af73639cc")

