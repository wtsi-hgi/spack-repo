# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnar(RPackage):
	"""Methods for Fitting Network Time Series Models

	Simulation of, and fitting models for, Generalised Network Autoregressive (GNAR) time series models which take account of network structure, potentially with exogenous variables.  Such models are described in Knight et al. (2020) <doi:10.18637/jss.v096.i05> and Nason and Wei (2021) <doi:10.1111/rssa.12875>.  Diagnostic tools for GNAR(X) models can be found in Nason et al (2023) <arXiv:2312.00530>.
	"""
	
	cran = "GNAR" 

	version("1.1.3", md5="d9ff107612e87d25fd568454c6d21d6b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
