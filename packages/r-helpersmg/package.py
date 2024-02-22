# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHelpersmg(RPackage):
	"""Tools for Environmental Analyses, Ecotoxicology and Various R
Functions

	Contains miscellaneous functions useful for managing 'NetCDF' files (see <https://en.wikipedia.org/wiki/NetCDF>), get moon phase and time for sun rise and fall, tide level, analyse and reconstruct periodic time series of temperature with irregular sinusoidal pattern, show scales and wind rose in plot with change of color of text, Metropolis-Hastings algorithm for Bayesian MCMC analysis, plot graphs or boxplot with error bars, search files in disk by there names or their content, read the contents of all files from a folder at one time.
	"""
	
	cran = "HelpersMG" 

	version("6.1", md5="9059d2453e611f4aab6f72e3ad5ff0a4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
