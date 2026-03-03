# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreedyepl(RPackage):
	"""Greedy Expected Posterior Loss

	Summarises a collection of partitions into a single optimal partition. The objective function is the expected posterior loss, and the minimisation is performed through a greedy algorithm described in Rastelli, R. and Friel, N. (2017) "Optimal Bayesian estimators for latent variable cluster models" <DOI:10.1007/s11222-017-9786-y>.
	"""
	
	cran = "GreedyEPL" 

	version("1.2", md5="cb4a3633dcb7754a9e80122b53657c2d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
