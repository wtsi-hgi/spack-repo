# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgraph(RPackage):
	"""Build Dependency Graphs using Projection

	Implements a general framework for creating dependency graphs using projection as introduced in Fan, Feng and Xia (2019)<arXiv:1501.01617>. Both lasso and sparse additive model projections are implemented. Both Pearson correlation and distance covariance options are available to generate the graph.
	"""
	
	cran = "pgraph" 

	version("1.6", md5="f8858582005722162a265a1eb528964a")

	depends_on("r-sam", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
