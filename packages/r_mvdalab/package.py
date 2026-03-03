# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvdalab(RPackage):
	"""Multivariate Data Analysis Laboratory

	An open-source implementation of latent variable methods and multivariate modeling tools. The focus is on exploratory analyses using dimensionality reduction methods including low dimensional embedding, classical multivariate statistical tools, and tools for enhanced interpretation of machine learning methods (i.e. intelligible models to provide important information for end-users).   Target domains include extension to dedicated applications e.g. for manufacturing process modeling, spectroscopic analyses, and data mining.
	"""
	
	cran = "mvdalab" 

	version("1.7", md5="3b3874874b9e110215ff5fe58afeb337")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
