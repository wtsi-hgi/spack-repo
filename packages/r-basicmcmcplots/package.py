# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasicmcmcplots(RPackage):
	"""Trace Plots, Density Plots and Chain Comparisons for MCMC
Samples

	Provides methods for examining posterior MCMC samples
    from a single chain using trace plots and density plots, and from
    multiple chains by comparing posterior medians and credible intervals
    from each chain.  These plotting functions have a variety of options,
    such as figure sizes, legends, parameters to plot, and saving plots to file.
    Functions interface with the NIMBLE software package, see
    de Valpine, Turek, Paciorek, Anderson-Bergman, Temple Lang and Bodik (2017)
    <doi:10.1080/10618600.2016.1172487>.
	"""
	
	cran = "basicMCMCplots" 

	version("0.2.7", md5="6cd49098e90dc47f212401c88683f07a")

	depends_on("r@3.4:", type=("build", "run"))
