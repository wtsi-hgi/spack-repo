# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVerso(RPackage):
	"""Viral Evolution ReconStructiOn (VERSO)

	Mutations that rapidly accumulate in viral genomes during a pandemic can be used to track the evolution of the virus and, accordingly, unravel the viral infection network. To this extent, sequencing samples of the virus can be employed to estimate models from genomic epidemiology and may serve, for instance, to estimate the proportion of undetected infected people by uncovering cryptic transmissions, as well as to predict likely trends in the number of infected, hospitalized, dead and recovered people. VERSO is an algorithmic framework that processes variants profiles from viral samples to produce phylogenetic models of viral evolution. The approach solves a Boolean Matrix Factorization problem with phylogenetic constraints, by maximizing a log-likelihood function. VERSO includes two separate and subsequent steps; in this package we provide an R implementation of VERSO STEP 1.
	"""
	
	homepage = "https://github.com/BIMIB-DISCo/VERSO"
	bioc = "VERSO"

	version("1.18.0", commit="8ef3b0838db0be295a9ddeea9df80bcf40ad0bda")
	version("1.12.0", commit="7bc4393ef4367f6ed91aa907e00746eaf1a14294")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
