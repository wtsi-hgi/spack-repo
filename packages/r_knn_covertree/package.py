# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnnCovertree(RPackage):
	"""An Accurate kNN Implementation with Multiple Distance Measures

	
    Similarly to the 'FNN' package, this package allows calculation of the k nearest neighbors (kNN) of a data matrix.
    The implementation is based on cover trees introduced by
    Alina Beygelzimer, Sham Kakade, and John Langford (2006) <doi:10.1145/1143844.1143857>.
	"""
	
	homepage = "https://github.com/flying-sheep/knn.covertree"
	cran = "knn.covertree" 

	version("1.0", md5="7e83d9a8c24a76eb60a3616e398f6f4f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
