# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItsmr(RPackage):
	"""Time Series Analysis Using the Innovations Algorithm

	Provides functions for modeling and forecasting time series data. Forecasting is based on the innovations algorithm. A description of the innovations algorithm can be found in the textbook "Introduction to Time Series and Forecasting" by Peter J. Brockwell and Richard A. Davis. <https://link.springer.com/book/10.1007/b97391>.
	"""
	
	homepage = "https://georgeweigt.github.io/itsmr-refman.pdf"
	cran = "itsmr" 

	version("1.10", md5="cdaa30b4cd28e1d01f39544949f543a3")

