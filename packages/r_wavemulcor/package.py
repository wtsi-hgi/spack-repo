# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWavemulcor(RPackage):
	"""Wavelet Routines for Global and Local Multiple Regression and
Correlation

	Wavelet routines that calculate single sets of wavelet
    multiple regressions and correlations, and cross-regressions and
    cross-correlations from a multivariate time series.  Dynamic versions
    of the routines allow the wavelet local multiple (cross-)regressions
    and (cross-)correlations to evolve over time.
	"""
	
	cran = "wavemulcor" 

	version("3.1.2", md5="c452e71213b5e42f2191b6015b13b737")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-waveslim@1.7.5:", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
