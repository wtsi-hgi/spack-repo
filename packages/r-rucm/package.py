# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRucm(RPackage):
	"""Implementation of Unobserved Components Model (UCM)

	Unobserved Components Models (introduced in Harvey, A. (1989),
    Forecasting, structural time series models and the Kalman filter, Cambridge
    New York: Cambridge University Press) decomposes a time series into
    components such as trend, seasonal, cycle, and the regression effects due
    to predictor series which captures the salient features of the series to
    predict its behavior.
	"""
	
	cran = "rucm" 

	version("0.6", md5="9255866e1b185155e2b32d1473d9f695")

	depends_on("r-kfas", type=("build", "run"))
