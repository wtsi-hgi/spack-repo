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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pmp_1.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pmp/pmp_1.14.1.tar.gz"]

	version("1.14.1", sha256="0b6b2129f968314740b8cfc02c564728ae03f10c47171ee146235d51d20df30f")
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
