# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsparse(RPackage):
	"""Statistical Learning on Sparse Matrices

	Implements many algorithms for statistical learning on 
  sparse matrices - matrix factorizations, matrix completion, 
  elastic net regressions, factorization machines. 
  Also 'rsparse' enhances 'Matrix' package by providing methods for 
  multithreaded <sparse, dense> matrix products and native slicing of 
  the sparse matrices in Compressed Sparse Row (CSR) format.
  List of the algorithms for regression problems:
  1) Elastic Net regression via Follow The Proximally-Regularized Leader (FTRL) 
  Stochastic Gradient Descent (SGD), as per McMahan et al(, <doi:10.1145/2487575.2488200>)
  2) Factorization Machines via SGD, as per Rendle (2010, <doi:10.1109/ICDM.2010.127>)
  List of algorithms for matrix factorization and matrix completion:
  1) Weighted Regularized Matrix Factorization (WRMF) via Alternating Least 
  Squares (ALS) - paper by Hu, Koren, Volinsky (2008, <doi:10.1109/ICDM.2008.22>)
  2) Maximum-Margin Matrix Factorization via ALS, paper by Rennie, Srebro 
  (2005, <doi:10.1145/1102351.1102441>)
  3) Fast Truncated Singular Value Decomposition (SVD), Soft-Thresholded SVD, 
  Soft-Impute matrix completion via ALS - paper by Hastie, Mazumder 
  et al. (2014, <arXiv:1410.2596>)
  4) Linear-Flow matrix factorization, from 'Practical linear models for 
  large-scale one-class collaborative filtering' by Sedhain, Bui, Kawale et al 
  (2016, ISBN:978-1-57735-770-4)
  5) GlobalVectors (GloVe) matrix factorization via SGD, paper by Pennington, 
  Socher, Manning (2014, <https://aclanthology.org/D14-1162/>)
  Package is reasonably fast and memory efficient - it allows to work with large
  datasets - millions of rows and millions of columns. This is particularly useful 
  for practitioners working on recommender systems.
	"""
	
	homepage = "https://github.com/rexyai/rsparse"
	cran = "rsparse" 

	version("0.5.1", md5="9060572ae998a45734ca452f347d2c5d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix@1.3:", type=("build", "run"))
	depends_on("r-matrixextra@0.1.7:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-float@0.2.2:", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-lgr@0.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.100.5:", type=("build", "run"))
