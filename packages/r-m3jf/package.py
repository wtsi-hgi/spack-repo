# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM3jf(RPackage):
	"""Multi-Modal Matrix Joint Factorization for Integrative
Multi-Omics Data Analysis

	Multi modality data matrices are factorized conjointly into the multiplication of a shared sub-matrix and multiple modality specific sub-matrices, group sparse constraint is applied to the shared sub-matrix to capture the homogeneous and heterogeneous information, respectively. Then the samples are classified by clustering the shared sub-matrix with kmeanspp(), a new version of kmeans() developed here to obtain concordant results. The package also provides the cluster number estimation by rotation cost. Moreover, cluster specific features could be retrieved using hypergeometric tests.
	"""
	
	cran = "M3JF" 

	version("0.1.0", md5="bf4d90b5ed4d989e2e3317c7f4d7fdbd")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-snftool", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-intersim", type=("build", "run"))
