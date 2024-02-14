# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsearray(RPackage):
	"""Efficient in-memory representation of multidimensional sparse arrays

	The SparseArray package is an infrastructure package that provides an array-like container for efficient in-memory representation of multidimensional sparse data in R. The package defines the SparseArray virtual class and two concrete subclasses: COO_SparseArray and SVT_SparseArray. Each subclass uses its own internal representation of the nonzero multidimensional data, the "COO layout" and the "SVT layout", respectively. SVT_SparseArray objects mimic as much as possible the behavior of ordinary matrix and array objects in base R. In particular, they suppport most of the "standard matrix and array API" defined in base R and in the matrixStats package from CRAN.
	"""
	
	homepage = "https://bioconductor.org/packages/SparseArray"
	bioc = "SparseArray" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SparseArray_1.2.3.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SparseArray/SparseArray_1.2.3.tar.gz"]

	version("1.2.3", md5="86224ea83ca5df5984cfc6907c8f0bc1")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics@0.43.1:", type=("build", "run"))
	depends_on("r-matrixgenerics@1.11.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-s4arrays@1.1.6:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
