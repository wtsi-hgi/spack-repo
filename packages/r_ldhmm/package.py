# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdhmm(RPackage):
	"""Hidden Markov Model for Financial Time-Series Based on Lambda
Distribution

	Hidden Markov Model (HMM) based on symmetric lambda distribution
    framework is implemented for the study of return time-series in the financial
    market. Major features in the S&P500 index, such as regime identification,
    volatility clustering, and anti-correlation between return and volatility,
    can be extracted from HMM cleanly. Univariate symmetric lambda distribution
    is essentially a location-scale family of exponential power distribution.
    Such distribution is suitable for describing highly leptokurtic time series
    obtained from the financial market. It provides a theoretically solid foundation
    to explore such data where the normal distribution is not adequate. The HMM
    implementation follows closely the book: "Hidden Markov Models for Time Series",
    by Zucchini, MacDonald, Langrock (2016).
	"""
	
	homepage = "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2979516"
	cran = "ldhmm" 

	version("0.6.1", md5="96c5928f52dbdff44bd2f98a74ca8b77")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-gnorm", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-xts@0.10.0:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
