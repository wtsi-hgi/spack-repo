# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM2smjf(RPackage):
	"""Multi-Modal Similarity Matrix Joint Factorization

	A new method to implement clustering from multiple modality data of certain samples, 
    the function M2SMjF() jointly factorizes multiple similarity matrices into a shared sub-matrix 
    and several modality private sub-matrices, which is further used for clustering. Along with 
    this method, we also provide function to calculate the similarity matrix and function to 
    evaluate the best cluster number from the original data.
	"""
	
	cran = "M2SMJF" 

	version("1.0", md5="85c256262f6c9fb37f6cd5fac80e0084")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
