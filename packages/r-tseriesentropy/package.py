# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTseriesentropy(RPackage):
	"""Entropy Based Analysis and Tests for Time Series

	Implements an Entropy measure of dependence based on the Bhattacharya-Hellinger-Matusita distance. Can be used as a (nonlinear) autocorrelation/crosscorrelation function for continuous and categorical time series. The package includes tests for serial and cross dependence and nonlinearity based on it. Some routines have a parallel version that can be used in a multicore/cluster environment. The package makes use of S4 classes.
	"""
	
	cran = "tseriesEntropy" 

	version("0.7-2", md5="bcc1e55eef09dd0899aac19f45e33084")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
