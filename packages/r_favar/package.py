# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFavar(RPackage):
	"""Bayesian Analysis of a FAVAR Model

	Estimate a FAVAR model by a Bayesian method, based on Bernanke et al. (2005) <DOI:10.1162/0033553053327452>.
	"""
	
	cran = "FAVAR" 

	version("0.1.3", md5="420223390ee06dc3ad03cef9f40f371e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bvartools", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
