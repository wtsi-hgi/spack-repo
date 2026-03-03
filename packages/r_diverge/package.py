# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiverge(RPackage):
	"""Evolutionary Trait Divergence Between Sister Species and Other
Paired Lineages

	Compares the fit of alternative models of continuous trait differentiation between sister species and other paired lineages. Differences in trait means between two lineages arise as they diverge from a common ancestor, and alternative processes of evolutionary divergence are expected to leave unique signatures in the distribution of trait differentiation in datasets comprised of many lineage pairs. Models include approximations of divergent selection, drift, and stabilizing selection. A variety of model extensions facilitate the testing of process-to-pattern hypotheses. Users supply trait data and divergence times for each lineage pair. The fit of alternative models is compared in a likelihood framework.
	"""
	
	cran = "diverge" 

	version("2.0.6", md5="e357fc0a269a9aa691aa5bbf51d49b33")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
