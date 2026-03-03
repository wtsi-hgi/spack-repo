# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastrg(RPackage):
	"""Sample Generalized Random Dot Product Graphs in Linear Time

	Samples generalized random product graphs, a generalization of
    a broad class of network models. Given matrices X, S, and Y with with
    non-negative entries, samples a matrix with expectation X S Y^T and
    independent Poisson or Bernoulli entries using the fastRG algorithm of
    Rohe et al. (2017) <https://www.jmlr.org/papers/v19/17-128.html>. The
    algorithm first samples the number of edges and then puts them down
    one-by-one.  As a result it is O(m) where m is the number of edges, a
    dramatic improvement over element-wise algorithms that which require
    O(n^2) operations to sample a random graph, where n is the number of
    nodes.
	"""
	
	homepage = "https://rohelab.github.io/fastRG/"
	cran = "fastRG" 

	version("0.3.2", md5="aa1a9557f52f9a96d9521ef6f7cfaa8a")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
