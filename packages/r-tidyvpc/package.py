# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyvpc(RPackage):
	"""VPC Percentiles and Prediction Intervals

	Perform a Visual Predictive Check (VPC), while accounting for 
    stratification, censoring, and prediction correction. Using piping from 
    'magrittr', the intuitive syntax gives users a flexible and powerful method 
    to generate VPCs using both traditional binning and a new binless approach 
    Jamsen et al. (2018) <doi:10.1002/psp4.12319> with Additive Quantile 
    Regression (AQR) and Locally Estimated Scatterplot Smoothing (LOESS) 
    prediction correction. 
	"""
	
	homepage = "https://github.com/certara/tidyvpc"
	cran = "tidyvpc" 

	version("1.5.1", md5="74967c2cabf413140b2f1ad3188cf0d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-quantreg@5.51:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
