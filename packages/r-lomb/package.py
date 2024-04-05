# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLomb(RPackage):
	"""Lomb-Scargle Periodogram

	Computes the Lomb-Scargle Periodogram and actogram for evenly or unevenly sampled time series. Includes a randomization procedure to obtain exact p-values. Partially based on C original by Press et al. (Numerical Recipes) and the Python module Astropy. For more information see Ruf, T. (1999). The Lomb-Scargle periodogram in biological rhythm research: analysis of incomplete and unequally spaced time-series. Biological Rhythm Research, 30(2), 178-201.
	"""
	
	cran = "lomb" 

	version("2.5.0", md5="2edb3c018b31098ce16f4316ea459636")
	version("2.2.0", md5="bdb906cbcaaa7d2f1307818f5365dec7")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
