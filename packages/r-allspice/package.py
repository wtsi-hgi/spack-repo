# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllspice(RPackage):
	"""RNA-Seq Profile Classifier

	We developed a lightweight machine learning tool for RNA profiling of acute lymphoblastic leukemia (ALL), however, it can be used for any problem where multiple classes need to be identified from multi-dimensional data. The methodology is described in Makinen V-P, Rehn J, Breen J, Yeung D, White DL (2022) Multi-cohort transcriptomic subtyping of B-cell acute lymphoblastic leukemia, International Journal of Molecular Sciences 23:4574, <doi:10.3390/ijms23094574>. The classifier contains optimized mean profiles of the classes (centroids) as observed in the training data, and new samples are matched to these centroids using the shortest Euclidean distance. Centroids derived from a dataset of 1,598 ALL patients are included, but users can train the models with their own data as well. The output includes both numerical and visual presentations of the classification results. Samples with mixed features from multiple classes or atypical values are also identified.
	"""
	
	cran = "Allspice" 

	version("1.0.7", md5="cc3a0e9b60b5bb8c86b8686a90b44be7")

