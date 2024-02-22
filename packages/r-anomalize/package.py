# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnomalize(RPackage):
	"""Tidy Anomaly Detection

	
    The 'anomalize' package enables a "tidy" workflow for detecting anomalies in data.
    The main functions are time_decompose(), anomalize(), and time_recompose().
    When combined, it's quite simple to decompose time series, detect anomalies,
    and create bands separating the "normal" data from the anomalous data at scale (i.e. for multiple time series). 
    Time series decomposition is used to remove trend and seasonal components via the time_decompose() function
    and methods include seasonal decomposition of time series by Loess ("stl") and 
    seasonal decomposition by piecewise medians ("twitter"). The anomalize() function implements
    two methods for anomaly detection of residuals including using an inner quartile range ("iqr")
    and generalized extreme studentized deviation ("gesd"). These methods are based on
    those used in the 'forecast' package and the Twitter 'AnomalyDetection' package. 
    Refer to the associated functions for specific references for these methods. 
	"""
	
	homepage = "https://github.com/business-science/anomalize"
	cran = "anomalize" 

	version("0.3.0", md5="d5ba568f2af196a67e114a942d143268")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-timetk", type=("build", "run"))
	depends_on("r-sweep", type=("build", "run"))
	depends_on("r-tibbletime@0.1.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
