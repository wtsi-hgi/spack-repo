# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixextra(RPackage):
	"""Extra Methods for Sparse Matrices

	Extends sparse matrix and vector classes from the 'Matrix' package by providing: 
  (a) Methods and operators that work natively on CSR formats (compressed sparse row, 
  a.k.a. 'RsparseMatrix') such as slicing/sub-setting, assignment, rbind(), 
  mathematical operators for CSR and COO such as addition ("+") or sqrt(), and methods such as diag(); 
  (b) Multi-threaded matrix multiplication and cross-product for many <sparse, dense> types, 
  including the 'float32' type from 'float'; 
  (c) Coercion methods between pairs of classes which are not present in 'Matrix', 
  such as 'dgCMatrix' -> 'ngRMatrix', as well as convenience conversion functions; 
  (d) Utility functions for sparse matrices such as sorting the indices or removing 
  zero-valued entries; 
  (e) Fast transposes that work by outputting in the opposite storage format;
  (f) Faster replacements for many 'Matrix' methods for all sparse types, such as
  slicing and elementwise multiplication.
  (g) Convenience functions for sparse objects, such as 'mapSparse' or a shorter 'show' method.
	"""
	
	homepage = "https://github.com/david-cortes/MatrixExtra"
	cran = "MatrixExtra" 

	version("0.1.15", md5="ba2eeff74b764fcbfef95690a376c755")

	depends_on("r-matrix@1.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-float", type=("build", "run"))
