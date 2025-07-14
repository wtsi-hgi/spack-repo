# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmp(RPackage):
	"""Peak Matrix Processing and signal batch correction for metabolomics datasets

	Methods and tools for (pre-)processing of metabolomics datasets (i.e. peak matrices), including filtering, normalisation, missing value imputation, scaling, and signal drift and batch effect correction methods. Filtering methods are based on: the fraction of missing values (across samples or features); Relative Standard Deviation (RSD) calculated from the Quality Control (QC) samples; the blank samples. Normalisation methods include Probabilistic Quotient Normalisation (PQN) and normalisation to total signal intensity. A unified user interface for several commonly used missing value imputation algorithms is also provided. Supported methods are: k-nearest neighbours (knn), random forests (rf), Bayesian PCA missing value estimator (bpca), mean or median value of the given feature and a constant small value. The generalised logarithm (glog) transformation algorithm is available to stabilise the variance across low and high intensity mass spectral features. Finally, this package provides an implementation of the Quality Control-Robust Spline Correction (QCRSC) algorithm for signal drift and batch effect correction of mass spectrometry-based datasets.
	"""
	
	bioc = "pmp"

	version("1.20.0", commit="3151807a03c97c54355dff7b01d619bb55e309ee")
	version("1.14.1", commit="5a67cc6512ff439d820f17b34407e4c87e32bd93")
	version("1.14.0", md5="07feec54f330f10904aae29238f79369")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
