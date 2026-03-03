# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStablespec(RPackage):
	"""Stable Specification Search in Structural Equation Models

	An exploratory and heuristic approach for specification search in
    Structural Equation Modeling. The basic idea is to subsample the original data
    and then search for optimal models on each subset. Optimality is defined through
    two objectives: model fit and parsimony. As these objectives are conflicting,
    we apply a multi-objective optimization methods, specifically NSGA-II, to obtain
    optimal models for the whole range of model complexities. From these optimal
    models, we consider only the relevant model specifications (structures), i.e.,
    those that are both stable (occur frequently) and parsimonious and use those to
    infer a causal model.
	"""
	
	homepage = "https://github.com/rahmarid/stablespec"
	cran = "stablespec" 

	version("0.3.0", md5="b6872bdf8db7df82c276abb5ad55bb86")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggm", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-sem", type=("build", "run"))
	depends_on("r-nsga2r", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
