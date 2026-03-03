# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsselect(RPackage):
	"""Execution of Time Series Models

	Execution of various time series models and choosing the best one
    either by a specific error metric or by picking the best one by majority vote.
    The models are based on the "forecast" package, written by Prof. Rob Hyndman.
	"""
	
	cran = "tsSelect" 

	version("0.1.8", md5="3166a1f8a7f551a0cb01906ac9014a9b")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
