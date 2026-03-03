# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClickb(RPackage):
	"""Web Data Analysis by Bayesian Mixture of Markov Models

	Designed for web usage data analysis, it implements tools to process web sequences and identify web browsing profiles through sequential classification. Sequences' clusters are identified by using a model-based approach, specifically mixture of discrete time first-order Markov models for categorical web sequences. A Bayesian approach is used to estimate model parameters and identify sequences classification as proposed by Fruehwirth-Schnatter and Pamminger (2010) <doi:10.1214/10-BA606>.
	"""
	
	cran = "clickb" 

	version("0.1", md5="8754455cee782319239fc7148214a8e3")

	depends_on("r-discreteweibull", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
