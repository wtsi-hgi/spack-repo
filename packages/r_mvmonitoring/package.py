# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvmonitoring(RPackage):
	"""Multi-State Adaptive Dynamic Principal Component Analysis for
Multivariate Process Monitoring

	Use multi-state splitting to apply Adaptive-Dynamic PCA (ADPCA) to
    data generated from a continuous-time multivariate industrial or natural
    process. Employ PCA-based dimension reduction to extract linear combinations
    of relevant features, reducing computational burdens. For a description of 
    ADPCA, see <doi:10.1007/s00477-016-1246-2>, the 2016 paper from Kazor et al.
    The multi-state application of ADPCA is from a manuscript under current
    revision entitled "Multi-State Multivariate Statistical Process Control" by
    Odom, Newhart, Cath, and Hering, and is  expected to appear in Q1 of 2018.
	"""
	
	homepage = "https://github.com/gabrielodom/mvMonitoring"
	cran = "mvMonitoring" 

	version("0.2.4", md5="07a93ffd0215db3f385aeb0436799dca")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
