# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR6causal(RPackage):
	"""R6 Class for Structural Causal Models

	The implemented R6 class 'SCM' aims to simplify working with structural causal models. The missing data mechanism can be defined as a part of the structural model. The class contains methods for 1) defining a structural causal model via functions, text or conditional probability tables, 2) printing basic information on the model, 3) plotting the graph for the model using packages 'igraph' or 'qgraph', 4) simulating data from the model, 5) applying an intervention, 6) checking the identifiability of a query using the R packages 'causaleffect' and 'dosearch', 7) defining the missing data mechanism, 8) simulating incomplete data from the model according to the specified missing data mechanism and 9) checking the identifiability in a missing data problem using the R package 'dosearch'. In addition, there are functions for running experiments and doing counterfactual inference using simulation.
	"""
	
	cran = "R6causal" 

	version("0.8.3", md5="6306c810132f3faa705e9e0abe78d2e8")
	version("0.8.2", md5="45078c5d55648e410b2d0ef26159c769")

	depends_on("r-causaleffect", type=("build", "run"))
	depends_on("r-cfid", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dosearch", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
