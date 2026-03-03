# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegspec(RPackage):
	"""Non-Parametric Bayesian Spectrum Estimation for Multirate Data

	Computes linear Bayesian spectral estimates from multirate	data for second-order stationary time series. Provides credible intervals and methods for plotting various spectral estimates. Please see the paper `Should we sample a time series more frequently?' (doi below) for a full description of and motivation for the methodology.
	"""
	
	homepage = "https://doi.org/10.1111/rssa.12210"
	cran = "regspec" 

	version("2.7", md5="273903c2a362670990941ccbfb32f987")

