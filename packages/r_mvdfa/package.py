# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvdfa(RPackage):
	"""Multivariate Detrended Fluctuation Analysis

	This R package provides an implementation of multivariate extensions of a well-known fractal analysis technique, Detrended Fluctuations Analysis (DFA; Peng et al., 1995<doi:10.1063/1.166141>), for multivariate time series: multivariate DFA (mvDFA). Several coefficients are implemented that take into account the correlation structure of the multivariate time series to varying degrees. These coefficients may be used to analyze long memory and changes in the dynamic structure that would by univariate DFA. Therefore, this R package aims to extend and complement the original univariate DFA (Peng et al., 1995) for estimating the scaling properties of nonstationary time series.
	"""
	
	homepage = "https://github.com/jpirmer/mvDFA"
	cran = "mvDFA" 

	version("0.0.4", md5="bac520af606b932ea7d30948969823a5")

	depends_on("r-longmemo", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-robper", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
