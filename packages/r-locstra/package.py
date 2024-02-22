# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocstra(RPackage):
	"""Fast Implementation of (Local) Population Stratification Methods

	Fast implementations to compute the genetic covariance matrix, the Jaccard similarity matrix, the s-matrix (the weighted Jaccard similarity matrix), and the (classic or robust) genomic relationship matrix of a (dense or sparse) input matrix (see Hahn, Lutz, Hecker, Prokopenko, Cho, Silverman, Weiss, and Lange (2020) <doi:10.1002/gepi.22356>). Full support for sparse matrices from the R-package 'Matrix'. Additionally, an implementation of the power method (von Mises iteration) to compute the largest eigenvector of a matrix is included, a function to perform an automated full run of global and local correlations in population stratification data, a function to compute sliding windows, and a function to invert minor alleles and to select those variants/loci exceeding a minimal cutoff value. New functionality in locStra allows one to extract the k leading eigenvectors of the genetic covariance matrix, Jaccard similarity matrix, s-matrix, and genomic relationship matrix via fast PCA without actually computing the similarity matrices. The fast PCA to compute the k leading eigenvectors can now also be run directly from 'bed'+'bim'+'fam' files.
	"""
	
	cran = "locStra" 

	version("1.9", md5="2a98a7fb0f51061671285864ebd7a3eb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-bigsnpr", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
