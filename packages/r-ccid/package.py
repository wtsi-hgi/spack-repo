# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcid(RPackage):
	"""Cross-Covariance Isolate Detect: a New Change-Point Method for
Estimating Dynamic Functional Connectivity

	Provides efficient implementation of the Cross-Covariance
    Isolate Detect (CCID) methodology for the estimation of the number
    and location of multiple change-points in the second-order
    (cross-covariance or network) structure of multivariate, possibly
    high-dimensional time series. The method is motivated by the detection
    of change points in functional connectivity networks for functional
    magnetic resonance imaging (fMRI), electroencephalography (EEG),
    magentoencephalography (MEG) and electrocorticography (ECoG) data. The
    main routines in the package have been extensively tested on fMRI data. 
    For details on the CCID methodology, please see Anastasiou et
    al (2022), Cross-covariance isolate detect: A new change-point method for
    estimating dynamic functional connectivity. Medical Image Analysis, Volume
    75.
	"""
	
	homepage = "https://github.com/Anastasiou-Andreas/ccid"
	cran = "ccid" 

	version("1.2.0", md5="bd5de8911f4a8282b90ee4931bf59fa1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-idetect", type=("build", "run"))
	depends_on("r-hdbinseg", type=("build", "run"))
	depends_on("r-genenet", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
