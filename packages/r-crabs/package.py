# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrabs(RPackage):
	"""Congruent Rate Analyses in Birth-Death Scenarios

	Features tools for exploring congruent phylogenetic birth-death models. It can construct the pulled speciation- and net-diversification rates from a reference model. Given alternative speciation- or extinction rates, it can construct new models that are congruent with the reference model. Functionality is included to sample new rate functions, and to visualize the distribution of one congruence class. See also Louca & Pennell (2020) <doi:10.1038/s41586-020-2176-1>.
	"""
	
	homepage = "https://github.com/afmagee/CRABS"
	cran = "CRABS" 

	version("1.2.0", md5="fc3a6a9b196555124f371c16b1816c2e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
