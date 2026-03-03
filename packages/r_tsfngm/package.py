# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsfngm(RPackage):
	"""Time Series Forecasting using Nonlinear Growth Models

	Nonlinear growth models are extremely useful in gaining insight into the underlying mechanism. These models are generally 'mechanistic,' with parameters that have biological meaning. This package allows you to fit and forecast time series data using nonlinear growth models. 
	"""
	
	cran = "tsfngm" 

	version("0.1.0", md5="9c810a691f0789c0563158ceb8da3c1c")

	depends_on("r@2.6:", type=("build", "run"))
