# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM2smf(RPackage):
	"""Multi-Modal Similarity Matrix Factorization for Integrative
Multi-Omics Data Analysis

	A new method to implement clustering from multiple modality data of certain samples, 
    the function M2SMF() jointly factorizes multiple similarity matrices into a shared sub-matrix 
    and several modality private sub-matrices, which is further used for clustering. Along with 
    this method, we also provide function to calculate the similarity matrix and function to 
    evaluate the best cluster number from the original data.
	"""
	
	cran = "M2SMF" 

	version("2.0", md5="81602452847d3c648a8ff9e8b755ce16")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
