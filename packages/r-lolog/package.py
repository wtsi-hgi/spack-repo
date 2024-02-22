# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLolog(RPackage):
	"""Latent Order Logistic Graph Models

	Estimation of Latent Order Logistic (LOLOG) Models for Networks.
    LOLOGs are a flexible and fully general class of statistical graph models. 
    This package provides functions for performing MOM, GMM and variational 
    inference. Visual diagnostics and goodness of fit metrics are provided. 
    See Fellows (2018) <arXiv:1804.04583> for a detailed description of the methods.
	"""
	
	homepage = "https://github.com/statnet/lolog"
	cran = "lolog" 

	version("1.3.1", md5="ad5c7dcca2f91ce86b9802c0734ab9e7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
