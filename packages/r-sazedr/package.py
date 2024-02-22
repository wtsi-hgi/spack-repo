# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSazedr(RPackage):
	"""Parameter-Free Domain-Agnostic Season Length Detection in Time
Series

	Spectral and Average Autocorrelation Zero Distance Density
    ('sazed') is a method for estimating the season length of a 
    seasonal time series. 'sazed' is aimed at practitioners, as it employs only 
    domain-agnostic preprocessing and does not depend on parameter tuning or 
    empirical constants. The computation of 'sazed' relies on the efficient 
    autocorrelation computation methods suggested by Thibauld Nion (2012, URL: 
    <https://etudes.tibonihoo.net/literate_musing/autocorrelations.html>) and by 
    Bob Carpenter (2012, URL: 
    <https://lingpipe-blog.com/2012/06/08/autocorrelation-fft-kiss-eigen/>).
	"""
	
	homepage = "https://github.com/mtoller/autocorr_season_length_detection/"
	cran = "sazedR" 

	version("2.0.2", md5="281ce04756d31b4fcd8f7db4bdc36c81")

	depends_on("r-bspec@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-fftwtools@0.9.8:", type=("build", "run"))
	depends_on("r-pracma@2.1.4:", type=("build", "run"))
	depends_on("r-zoo@1.8.3:", type=("build", "run"))
