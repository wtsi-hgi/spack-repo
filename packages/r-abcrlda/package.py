# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbcrlda(RPackage):
	"""Asymptotically Bias-Corrected Regularized Linear Discriminant
Analysis

	Offers methods to perform asymptotically bias-corrected regularized linear discriminant analysis (ABC_RLDA) for cost-sensitive binary classification. The bias-correction is an estimate of the bias term added to regularized discriminant analysis (RLDA) that minimizes the overall risk. The default magnitude of misclassification costs are equal and set to 0.5; however, the package also offers the options to set them to some predetermined values or, alternatively, take them as hyperparameters to tune.
    A. Zollanvari, M. Abdirash, A. Dadlani and B. Abibullaev (2019) <doi:10.1109/LSP.2019.2918485>.
	"""
	
	homepage = "https://ieeexplore.ieee.org/document/8720003/"
	cran = "abcrlda" 

	version("1.0.3", md5="651e6e18e08916b443aaf011b5a63525")

