# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDchaos(RPackage):
	"""Chaotic Time Series Analysis

	Chaos theory has been hailed as a revolution of thoughts and attracting ever increasing 
    attention of many scientists from diverse disciplines. Chaotic systems are nonlinear deterministic 
    dynamic systems which can behave like an erratic and apparently random motion. A relevant field
    inside chaos theory and nonlinear time series analysis is the detection of a chaotic behaviour 
    from empirical time series data. One of the main features of chaos is the well known initial value 
    sensitivity property. Methods and techniques related to test the hypothesis of chaos try to quantify 
    the initial value sensitive property estimating the Lyapunov exponents. The DChaos package 
    provides different useful tools and efficient algorithms which test robustly the hypothesis of chaos 
    based on the Lyapunov exponent in order to know if the data generating process behind time series 
    behave chaotically or not.
	"""
	
	cran = "DChaos" 

	version("0.1-7", md5="b352a30b3840a995095926132c56ad48")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
