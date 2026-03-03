# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantkriging(RPackage):
	"""Quantile Kriging for Stochastic Simulations with Replication

	A re-implementation of quantile kriging. Quantile kriging was described by Plumlee and Tuo (2014) <doi:10.1080/00401706.2013.860919>.  With computational savings when dealing with replication from the recent paper by Binois, Gramacy, and Ludovski (2018) <doi:10.1080/10618600.2018.1458625> it is now possible to apply quantile kriging to a wider class of problems.  In addition to fitting the model, other useful tools are provided such as the ability to automatically perform leave-one-out cross validation.
	"""
	
	cran = "quantkriging" 

	version("0.1.0", md5="345ea4d8cd41d86e0923a3d1de594abc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-hetgp@1.1.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.17:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
