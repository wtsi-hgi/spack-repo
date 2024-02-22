# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpinetr(RPackage):
	"""Epistatic Network Modelling with Forward-Time Simulation

	Allows for forward-in-time simulation of epistatic networks with associated
    phenotypic output.
	"""
	
	homepage = "https://github.com/diondetterer/epinetr"
	cran = "epinetr" 

	version("0.96", md5="56806baa7033f0dd4f92c27f5d6e0450")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ga@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-igraph@1.2.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppalgos@2.4.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-vcfr@1.8:", type=("build", "run"))
