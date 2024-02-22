# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvthresh(RPackage):
	"""Level-Dependent Cross-Validation Thresholding

	The level-dependent cross-validation method is implemented
        for the selection of thresholding
        value in wavelet shrinkage. This procedure is implemented
        by coupling a conventional cross validation with an
        imputation method due to a limitation of data length,
        a power of 2. It can be easily applied to classical
        leave-one-out and k-fold cross validation.
        Since the procedure is computationally fast,
        a level-dependent cross validation can be performed for
        wavelet shrinkage of various data such as a data
        with correlated errors.
	"""
	
	cran = "CVThresh" 

	version("1.1.2", md5="2449629aab64fbbbd0e5cc2ce1fdfbab")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-wavethresh@4.6.1:", type=("build", "run"))
	depends_on("r-ebayesthresh@1.3.2:", type=("build", "run"))
