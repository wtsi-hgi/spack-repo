# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpsmooth(RPackage):
	"""Data Sets from "Forecasting with Exponential Smoothing"

	Data sets from the book "Forecasting with exponential smoothing: the state space approach" by 
	Hyndman, Koehler, Ord and Snyder (Springer, 2008).
	"""
	
	homepage = "https://github.com/robjhyndman/expsmooth"
	cran = "expsmooth" 

	version("2.3", md5="93e2dac942f345459019de29359662e7")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
