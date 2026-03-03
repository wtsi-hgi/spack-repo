# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDarand(RPackage):
	"""Differential Analysis with Random Reference Genes

	Differential Analysis of short RNA transcripts that can be modeled by either Poisson or Negative binomial distribution.  The statistical methodology implemented in this package is based on the random selection of references genes (Desaulle et al. (2021) <arXiv:2103.09872>). 
	"""
	
	cran = "DArand" 

	version("0.0.1.2", md5="bb095ae81aaa2719ec82b7874e704691")

