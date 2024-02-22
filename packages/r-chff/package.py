# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChff(RPackage):
	"""Closest History Flow Field Forecasting for Bivariate Time Series

	The software matches the current history to the closest history in a time series to build a forecast.
	"""
	
	cran = "CHFF" 

	version("0.1.0", md5="1c46411ec2c7a230d599cd9883c1f0f6")

