# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchaeophases(RPackage):
	"""Post-Processing of the Markov Chain Simulated by 'ChronoModel',
'Oxcal' or 'BCal'

	Provides a list of functions for the statistical analysis of archaeological dates and groups of dates. It is based on the post-processing of the Markov Chains whose stationary distribution is the posterior distribution of a series of dates. Such output can be simulated by different applications as for instance 'ChronoModel' (see <https://chronomodel.com/>), 'Oxcal' (see <https://c14.arch.ox.ac.uk/oxcal.html>) or 'BCal' (see <https://bcal.shef.ac.uk/>). The only requirement is to have a csv file containing a sample from the posterior distribution.  Note that this package interacts with data available through the 'ArchaeoPhases.dataset' package which is available in a separate repository.  The size of the 'ArchaeoPhases.dataset' package is approximately 4 MB.
	"""
	
	cran = "ArchaeoPhases" 

	version("1.8", md5="f26e2b6148f44f023423153172c248ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-hdrcde", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-toordinal", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggalt", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
