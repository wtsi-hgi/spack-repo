# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotmcmc(RPackage):
	"""MCMC Diagnostic Plots

	Markov chain Monte Carlo diagnostic plots. The purpose of the
  package is to combine existing tools from the 'coda' and 'lattice' packages,
  and make it easy to adjust graphical details.
	"""
	
	cran = "plotMCMC" 

	version("2.0.1", md5="c5ba4f813285c5f6412037da30882a54")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
