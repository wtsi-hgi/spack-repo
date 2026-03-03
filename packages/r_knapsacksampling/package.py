# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnapsacksampling(RPackage):
	"""Generate Feasible Samples of a Knapsack Problem

	The sampl.mcmc function creates samples of the feasible region of a knapsack problem with both equalities and inequalities constraints.
	"""
	
	homepage = "https://github.com/chinsoon12/KnapsackSampling"
	cran = "KnapsackSampling" 

	version("0.1.1", md5="f85cc92d9d58288d834b47730bb4b210")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
