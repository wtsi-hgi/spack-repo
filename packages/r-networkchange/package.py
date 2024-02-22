# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkchange(RPackage):
	"""Bayesian Package for Network Changepoint Analysis

	Network changepoint analysis for undirected network data. The package implements a hidden Markov network change point model (Park and Sohn (2020)). Functions for break number detection using the approximate marginal likelihood and WAIC are also provided.
	"""
	
	homepage = "https://github.com/jongheepark/NetworkChange"
	cran = "NetworkChange" 

	version("0.8", md5="564a83d59245eb68e4c96d5c6385f321")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggvis", type=("build", "run"))
