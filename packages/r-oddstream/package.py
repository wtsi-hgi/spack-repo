# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROddstream(RPackage):
	"""Outlier Detection in Data Streams

	We proposes a framework that provides real time support for early detection of
    anomalous series within a large collection of streaming time series data. By definition, anomalies
    are rare in comparison to a system's typical behaviour. We define an anomaly as an observation that
    is very unlikely given the forecast distribution. The algorithm first forecasts a boundary for the
    system's typical behaviour using a representative sample of the typical behaviour of the system. An
    approach based on extreme value theory is used for this boundary prediction process. Then a sliding
    window is used to test for anomalous series within the newly arrived collection of series. Feature
    based representation of time series is used as the input to the model. To cope with concept drift,
    the forecast boundary for the system's typical behaviour is updated periodically.  More details
    regarding the algorithm can be found in Talagala, P. D., Hyndman, R. J., Smith-Miles, K., et al.
    (2019) <doi:10.1080/10618600.2019.1617160>.
	"""
	
	cran = "oddstream" 

	version("0.5.0", md5="57810a6687102096cac1ddc2ec1a0cea")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-mvtsplot", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
