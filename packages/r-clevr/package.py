# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClevr(RPackage):
	"""Clustering and Link Prediction Evaluation in R

	Tools for evaluating link prediction and clustering algorithms 
    with respect to ground truth. Includes efficient implementations of 
    common performance measures such as pairwise precision/recall, 
    cluster homogeneity/completeness, variation of information, 
    Rand index etc.
	"""
	
	homepage = "https://github.com/cleanzr/clevr"
	cran = "clevr" 

	version("0.1.2", md5="a0c073608d3de07ac705c1c457cf206b")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-bh@1.69:", type=("build", "run"))
