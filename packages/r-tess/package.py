# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTess(RPackage):
	"""Diversification Rate Estimation and Fast Simulation of
Reconstructed Phylogenetic Trees under Tree-Wide
Time-Heterogeneous Birth-Death Processes Including
Mass-Extinction Events

	Simulation of reconstructed phylogenetic trees under tree-wide time-heterogeneous birth-death processes and estimation of diversification parameters under the same model. Speciation and extinction rates can be any function of time and mass-extinction events at specific times can be provided. Trees can be simulated either conditioned on the number of species, the time of the process, or both. Additionally, the likelihood equations are implemented for convenience and can be used for Maximum Likelihood (ML) estimation and Bayesian inference.
	"""
	
	cran = "TESS" 

	version("2.1.2", md5="3fa19b491c62176bb9cdbb04a7564c4c")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
