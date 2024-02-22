# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveband(RPackage):
	"""Computes Credible Intervals for Bayesian Wavelet Shrinkage

	Computes Bayesian wavelet shrinkage credible intervals for
	nonparametric regression.
	The method uses cumulants to derive Bayesian credible intervals for
	wavelet regression estimates.
	The first four cumulants of the posterior distribution of the
	estimates are expressed in terms of the observed data and integer
	powers of the mother wavelet functions.
	These powers are closely approximated by linear combinations of
	wavelet scaling functions at an appropriate finer scale.
	Hence, a suitable modification of the discrete wavelet transform allows
	the posterior cumulants to be found efficiently for any data set.
	Johnson transformations then yield the credible intervals themselves.
	Barber, S., Nason, G.P. and Silverman, B.W. (2002)
	<doi:10.1111/1467-9868.00332>.
	"""
	
	cran = "waveband" 

	version("4.7.2", md5="6d53432af78fa9e901fe9510b78f0342")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-wavethresh@4.6:", type=("build", "run"))
