# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcts(RPackage):
	"""Periodically Correlated and Periodically Integrated Time Series

	Classes and methods for modelling and simulation of
    periodically correlated (PC) and periodically integrated time
    series.  Compute theoretical periodic autocovariances and related
    properties of PC autoregressive moving average models. Some original
    methods including Boshnakov & Iqelan (2009)
    <doi:10.1111/j.1467-9892.2009.00617.x>, Boshnakov (1996)
    <doi:10.1111/j.1467-9892.1996.tb00281.x>.
	"""
	
	homepage = "https://geobosh.github.io/pcts/"
	cran = "pcts" 

	version("0.15.7", md5="2e99adb41e570a0e159c9925b55ff49a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sarima", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-polynomf@2.0.2:", type=("build", "run"))
	depends_on("r-gbutils", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-lagged@0.2.2:", type=("build", "run"))
	depends_on("r-mcompanion@0.5.8:", type=("build", "run"))
	depends_on("r-rdpack@0.9:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
