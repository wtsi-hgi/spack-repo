# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigsparser(RPackage):
	"""Sparse Matrix Format with Data on Disk

	Provide a sparse matrix format with data stored on disk, to be
    used in both R and C++. This is intended for more efficient use of sparse 
    data in C++ and also when parallelizing, since data on disk does not need
    copying. Only a limited number of features will be implemented. For now,
    conversion can be performed from a 'dgCMatrix' or a 'dsCMatrix' from R 
    package 'Matrix'. A new compact format is also now available.
	"""
	
	homepage = "https://github.com/privefl/bigsparser"
	cran = "bigsparser" 

	version("0.6.1", md5="d60dc820e3fa4e24040e53c929abc9ad")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bigassertr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rmio", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
