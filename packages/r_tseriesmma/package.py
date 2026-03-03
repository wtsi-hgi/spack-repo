# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTseriesmma(RPackage):
	"""Multiscale Multifractal Analysis of Time Series Data

	Multiscale multifractal analysis (MMA) (Gierałtowski et al.,
    2012)<DOI:10.1103/PhysRevE.85.021915> is a time series analysis method,
    designed to describe scaling properties of fluctuations within the signal
    analyzed. The main result of this procedure is the so called Hurst surface
    h(q,s) , which is a dependence of the local Hurst exponent h (fluctuation
    scaling exponent) on the multifractal parameter q and the scale of observation s
    (data window width).
	"""
	
	cran = "TSeriesMMA" 

	version("0.1.1", md5="fcccf8a194475e35096b4f93bb76ae73")

	depends_on("r@3.0.2:", type=("build", "run"))
