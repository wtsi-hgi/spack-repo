# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcoutput(RPackage):
	"""Functions to Store, Manipulate and Display Markov Chain Monte
Carlo (MCMC) Output

	Implements a class ('mcmcOutput') for efficiently storing and handling Markov chain Monte Carlo (MCMC) output, intended as an aid for those writing customized MCMC samplers. A range of constructor methods are provided covering common output formats. Functions are provided to generate summary and diagnostic statistics and to display histograms or density plots of posterior distributions, for the entire output, or subsets of draws, nodes, or parameters.
	"""
	
	homepage = "https://github.com/mikemeredith/mcmcOutput"
	cran = "mcmcOutput" 

	version("0.1.3", md5="858f55a8438d75473af857375be708b2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
